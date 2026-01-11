from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Usercards
from core.models import Rarity


@login_required
def binder_view(request):
    """
    Renders the shop page with scheduled characters,
    combining model data, JSON metadata, and calculated
    attributes sorted by power.
    """
    page_url = "binder/binder.html"
    usercards = Usercards.objects.filter(owner=request.user)
    user_chars = []
    # Rarities set for unique character rarity values in the binder filter
    for char in usercards:
        character = char.character
        # Card data for each user card so the correct data can be displayed
        card_data = {
            "usercard": char,
            "chardetails": character,
            "json": character.get_legends_data(),
            "power": character.power_status(),
            "alignment": character.charc_alignment().capitalize(),
            "universe": character.charc_universe(),
            "rarity": character.rarity.name,
            "affiliation": character.group_affiliation(),
            "fullname": character.full_name()
        }
        user_chars.append(card_data)

    user_chars.sort(
        key=lambda character_data: character_data["power"],
        reverse=True
    )
    # Set comprehension for filter dropdown data
    alignments = {
        character_data["alignment"] for character_data in user_chars
    }
    universes = {
        character_data["universe"] for character_data in user_chars
    }
    rarities_filter = Rarity.unique_rarities_for_filter()

    context = {
        "characters": user_chars,
        "rarities": rarities_filter,
        "alignments": sorted(alignments),
        "universes": sorted(universes)
    }
    return render(request, page_url, context)
