"""
Views for the shop app.

This module defines the shop view, which determines which characters
are currently available for sale based on the active shop schedules.
It cross-references the database models with external legend data
to build a dynamic shop interface for display in the front-end template.
"""

from django.shortcuts import render
from django.utils import timezone
from core.data import datastore
from .models import ShopScheduler
from core.models import CharacterCard
import random


def shop_view(request):
    """
    Renders the shop page with characters available during the
    currently active schedule period.
    - Retrieves active shop schedules where the current
        time falls between start and end times.
    - Collects all scheduled items linked to those schedules.
    - Ensures that only characters marked as eligible for rotation
        are included.
    - Cross-references each eligible character with external data
        from datastore.legends to enrich their display information.
    - Calculates each character's total power score.
    - Sorts the final list alphabetically by character name.
    - Passes the sorted data to the shop template for rendering.

    Returns:
        HttpResponse: Rendered HTML page displaying the shop inventory.
    """
    page_url = "shop/shop.html"
    final_list = []
    now = timezone.now()
    active_schedules = ShopScheduler.objects.filter(
        start_time__lte=now,
        end_time__gte=now
    )
    if active_schedules:
        for schedule in active_schedules:
            scheduled_items = schedule.scheduled_items.all()
            for item in scheduled_items:
                if item.character.can_participate_in_rotation:
                    char_id = item.character.id
                    char = item.character
                    for legend in datastore.legends:
                        legend_id = legend["id"]
                        if legend_id == char_id:
                            total_power = sum(legend["powerstats"].values())
                            pair = {
                                "model": char,
                                "json": legend,
                                "power": total_power
                            }
                            final_list.append(pair)

    else:
        characters = CharacterCard.objects.all()
        char_list = list(characters)
        res = random.sample(char_list, 12)
        for char in res:
            char_id = char.id
            for legend in datastore.legends:
                legend_id = legend["id"]
                if legend_id == char_id:
                    total_power = sum(legend["powerstats"].values())
                    pair = {
                        "model": char,
                        "json": legend,
                        "power": total_power
                    }
                    final_list.append(pair)
    final_list.sort(key=lambda pair: pair["power"], reverse=True)

    context = {
        "characters": final_list
    }
    return render(request, page_url, context)
