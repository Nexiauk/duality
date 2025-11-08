"""
Views for the shop app.

This module defines the shop view, which determines which characters
are currently available for sale based on the active shop schedules.
It cross-references the database models with external legend data
to build a dynamic shop interface for display in the front-end template.
"""

from django.shortcuts import render
from .models import ShopScheduler
from core.models import CharacterCard


def shop_view(request):
    page_url = "shop/shop.html"
    scheduled_characters = []
    for schedule in ShopScheduler.get_or_create_active_schedule():
            eligible_character = schedule.get_eligible_characters()
            for char in eligible_character:
                character_data = {
                    "model": char,
                    "json": char.get_legends_data(),
                    "power": char.power_status()
                }
                scheduled_characters.append(character_data)
    context = {
        "characters": scheduled_characters
    }
    return render(request, page_url, context)
