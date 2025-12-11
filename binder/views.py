from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Usercards


def binder_view(request):
    """
    Renders the shop page with scheduled characters,
    combining model data, JSON metadata, and calculated
    attributes sorted by power.
    """
    page_url = "binder/binder.html"
    usercards = Usercards.objects.filter(owner=request.user)
    user_chars = []
    for char in usercards:
        character = char.character
        card_data = {
            "usercard": char,
            "chardetails": character,
            "json": character.get_legends_data(),
            "power": character.power_status(),
            "alignment": character.charc_alignment(),
            "universe": character.charc_universe()
            }
        user_chars.append(card_data)

    context = {
        "characters": user_chars
    }
    return render(request, page_url, context)
