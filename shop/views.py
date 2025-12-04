"""
Views for the shop app.

Retrieves or creates the active shop schedule, ensures its items are set up,
and gathers eligible characters for display. Characters are enriched with
their data and power status, sorted by power, and rendered to the shop page.
"""

from django.shortcuts import render, get_object_or_404, redirect
from .models import ShopScheduler, CharacterCard
from binder.models import Usercards
from django.contrib.auth.decorators import login_required
import stripe
from django.conf import settings
from django.urls import reverse


def shop_view(request):
    """
    Renders the shop page with scheduled characters,
    combining model data, JSON metadata, and calculated
    attributes sorted by power.
    """
    page_url = "shop/shop.html"
    scheduled_characters = []
    schedule = ShopScheduler.get_or_create_active_schedule()
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
    context = {
        "characters": scheduled_characters
    }
    return render(request, page_url, context)


@login_required
def card_view(request, id):
    """
    Renders the card detail page for a given CharacterCard
    including its JSON metadata and calculated power status.
    """
    card = get_object_or_404(CharacterCard, id=id)
    page_url = "shop/card-detail.html"
    json_data = card.get_legends_data()
    power = card.power_status()
    context = {
        "char": card,
        "json": json_data,
        "power": power
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
            cancel_url=request.build_absolute_uri(reverse('payment-cancel'))
        )
        return redirect(session.url, code=303)


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
            purchases = get_purchases_from_session(session)
            if session.payment_status == 'paid':
                for purchase in purchases:
                    Usercards.create_usercard(
                        request.user, purchase, session.payment_intent)
                return render(request, 'shop/success.html', {
                    'customer_email': session.customer_details.email,
                    'customer': customer,
                    'purchases': purchases
                })
            else:
                return render(request, 'shop/cancel.html')
        except Exception as e:
            return render(request, 'shop/error.html', {'error': str(e)})
    else:
        return render(
            request,
            'shop/error.html',
            {'error': 'No session id provided'}
            )


@login_required
def payment_cancel(request):
    return render(request, 'shop/cancel')


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
