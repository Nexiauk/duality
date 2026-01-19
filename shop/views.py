"""
Views for the shop app.

Retrieves or creates the active shop schedule, ensures its items are set up,
and gathers eligible characters for display. Characters are enriched with
their data and power status, sorted by power, and rendered to the shop page.
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from .models import ShopScheduler, CharacterCard
from core.models import Rarity
from binder.models import Usercards
import stripe
import smtplib


def shop_view(request):
    """
    Renders the shop page with scheduled characters,
    combining model data, JSON metadata, and calculated
    attributes sorted by power.
    Also grabs a list of the current user's owned cards
    for logic-based styling and disabling of the buy button.
    """
    page_url = "shop/shop.html"
    scheduled_characters = []
    schedule = ShopScheduler.get_or_create_active_schedule()
    if request.user.is_authenticated:
        owned_cards = Usercards.objects.filter(
            owner=request.user).values_list('character', flat=True)
    else:
        owned_cards = Usercards.objects.none()
    for s in schedule:
        if not s.get_items():
            s.create_items_for_schedule()
        eligible_character = s.get_eligible_characters()
        for char in eligible_character:
            character_data = {
                "model": char,
                "json": char.get_legends_data(),
                "power": char.power_status(),
                "alignment": char.charc_alignment(),
                "universe": char.charc_universe()
            }
            scheduled_characters.append(character_data)
    scheduled_characters.sort(
        key=lambda character_data: character_data["power"],
        reverse=True
    )
    rarities_filter = Rarity.unique_rarities_for_filter()
    alignments_filter = {
        character_data["alignment"] for character_data in scheduled_characters
    }
    universes_filter = {
        character_data["universe"] for character_data in scheduled_characters
    }
    context = {
        "characters": scheduled_characters,
        "rarities": rarities_filter,
        "alignments": sorted(alignments_filter),
        "universes": sorted(universes_filter),
        "owned_cards": owned_cards
    }
    return render(request, page_url, context)


@login_required
def card_view(request, id):
    """
    Renders the card detail page for a given CharacterCard
    including its JSON metadata and calculated power status.
    Checks the schedule to see if the card requested is in the shop,
    if not, sends the user back to the shop with a warning message.
    """
    schedule = ShopScheduler.get_or_create_active_schedule()
    eligible_cards = []
    for s in schedule:
        eligible_cards.extend(s.get_eligible_characters())
    card = get_object_or_404(CharacterCard, id=id)
    if card not in eligible_cards:
        messages.warning(
            request, "This card is not currently available in the shop")
        return redirect("shop")
    page_url = "shop/card-detail.html"
    json_data = card.get_legends_data()
    power = card.power_status()
    alignment = card.charc_alignment()
    universe = card.charc_universe()
    context = {
        "char": card,
        "json": json_data,
        "power": power,
        "alignment": alignment,
        "universe": universe
    }
    return render(request, page_url, context)


@login_required
def create_checkout(request, id):
    """
    Create a Stripe checkout session for purchasing a CharacterCard.

    Requires the user to be logged in. Retrieves the specified card by ID,
    calculates its price in pence, and creates a Stripe session with product
    details and user metadata. Redirects to the Stripe checkout page upon POST.
    """
    stripe.api_key = settings.STRIPE_SECRET_KEY
    success_url = request.build_absolute_uri(
        reverse('payment-success')) + '?session_id={CHECKOUT_SESSION_ID}'
    product = get_object_or_404(
        CharacterCard,
        id=id
    )
    # Stripe requires an integer field in pence for the price,
    # rarity.price is a decimal field
    price_in_pence = int(product.rarity.price * 100)
    json_data = product.get_legends_data()
    if request.method == 'POST':
        cancel_template = 'shop/cancel.html'
        try:
            session = stripe.checkout.Session.create(
                line_items=[
                    {'price_data': {
                        'currency': 'gbp',
                        'product_data': {
                            'name': product.name,
                            'images': [json_data['images']['lg']],
                            'metadata': {
                                    'character_id': product.id
                            }
                        },
                        'unit_amount': price_in_pence,
                    },
                        'quantity': 1}
                ],
                mode='payment',
                metadata={
                    'customer': request.user.username,
                },
                success_url=success_url,
                cancel_url=request.build_absolute_uri(
                    reverse('payment-cancel')
                    )
            )
            return redirect(session.url, code=303)
        # Handles declined cards
        except stripe.error.CardError as e:
            error_msg = f"Card Error: {str(e)}"
            return render(request, cancel_template, {'error': error_msg})
        # Handles invalid requests
        except stripe.error.InvalidRequestError as e:
            error_msg = f"Invalid Request: {str(e)}"
            return render(request, cancel_template, {'error': error_msg})
        # Handles Authentication failed
        except stripe.error.AuthenticationError as e:
            error_msg = (
                f"Authentication with payment provider failed: {str(e)}"
            )
            return render(request, cancel_template, {'error': error_msg})
        # Generic Stripe errors
        except stripe.error.StripeError as e:
            error_msg = f"Payment Error {str(e)}"
            return render(request, cancel_template, {'error': error_msg})
        # Network issues
        except stripe.error.APIConnectionError as e:
            error_msg = f"Network error. Please try again: {str(e)}"
            return render(request, cancel_template, {'error': error_msg})
        # Something else happened
        except Exception as e:
            error_msg = f"An error occurred: {str(e)}"
            return render(request, cancel_template, {'error': error_msg})


@login_required
def payment_success(request):
    """
    Handle successful Stripe payments and create user-owned cards.

    Retrieves the Stripe session using the session_id from the query string,
    verifies payment status, records purchased CharacterCards for the logged-in
    user, and renders a success page. If payment failed or an error occurs,
    renders the appropriate cancel or error page.
    """
    session_id = request.GET.get('session_id')
    if session_id:
        try:
            session = stripe.checkout.Session.retrieve(
                session_id,
                expand=['line_items.data.price.product']
            )
            customer = session.metadata.get('customer')
            customer_username = User.objects.get(username=customer)
            display_name = customer_username.get_display_name
            purchases = get_purchases_from_session(session)
            message = (
                f"{session.customer_details.name}, your purchase is complete."
                )
            if session.payment_status == 'paid':
                # Create user cards
                for purchase in purchases:
                    usercard = Usercards.create_usercard(
                        request.user, purchase, session.payment_intent)
                    purchase['order_reference'] = usercard.order_reference
                    purchase['price'] = purchase['price']/100
                    # Message variable for email text
                    message += (
                        f"- {purchase['character_name']} | "
                        f"£{purchase['price']} | "
                        f"Order Ref: {purchase['order_reference']}\n"
                        )
                # Send a confirmation email - customised to purchase made.
                try:
                    send_mail(
                        'Your Duality purchase was successful.',
                        message,
                        'admin@duality.com',
                        [session.customer_details.email],
                        fail_silently=False,
                    )
                except (BadHeaderError, smtplib.SMTPException) as e:
                    print(f"Email failed to send {e}")
                return render(request, 'shop/success.html', {
                    'customer_email': session.customer_details.email,
                    'customer': customer,
                    'purchases': purchases,
                    'display_name': display_name
                })
            else:
                return render(request, 'shop/cancel.html')
        except Exception as e:
            return render(request, 'shop/cancel.html', {'error': str(e)})
    else:
        return render(
            request,
            'shop/cancel.html',
            {'error': 'No session id provided'}
        )


@login_required
def payment_cancel(request):
    """Returns the payment cancellation template"""
    return render(request, 'shop/cancel.html')


def get_purchases_from_session(session):
    """
    Extract purchased item details from a Stripe checkout session.

    Returns a list of dictionaries containing the price, character ID,
    and character name for each item in the session's line items.
    """
    purchases = []
    for item in session.line_items.data:
        purchases.append({
            'price': item.price.unit_amount,
            'character_id': item.price.product.metadata.get('character_id'),
            'character_name': item.price.product.name
        })
    return purchases
