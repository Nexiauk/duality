"""
Views for the shop app.

Retrieves or creates the active shop schedule, ensures its items are set up,
and gathers eligible characters for display. Characters are enriched with
their data and power status, sorted by power, and rendered to the shop page.
"""

from django.shortcuts import render
from .models import ShopScheduler
from core.models import CharacterCard


def shop_view(request):
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
                "alignment": char.charc_alignment()
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
