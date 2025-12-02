"""
Views for the shop app.

Retrieves or creates the active shop schedule, ensures its items are set up,
and gathers eligible characters for display. Characters are enriched with
their data and power status, sorted by power, and rendered to the shop page.
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import ShopScheduler
from core.models import CharacterCard
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

stripe.api_key=settings.STRIPE_SECRET_KEY

@login_required
def create_checkout(request, id):
    product = get_object_or_404(CharacterCard, id=id)
    price_in_pence=int(product.rarity.price * 100)
    json_data=product.get_legends_data()
    if request.method=='POST':
        session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data':{
                        'currency': 'gbp',
                        'product_data': {
                            'name': product.name,
                            'images':[json_data['images']['lg']]
                        },
                        'unit_amount': price_in_pence,
                    },
                    'quantity':1,
                }
            ],
            mode='payment',
            success_url=request.build_absolute_uri(reverse('payment-success')),
            cancel_url=request.build_absolute_uri(reverse('payment-cancel'))
        )
        return redirect(session.url, code=303)
    
def payment_success(request):
    return render(request, 'shop/success.html')

def payment_cancel(request):
    return render(request, 'shop/cancel.html')


