from django.shortcuts import render
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
        # Rarities set for unique character rarity values in the binder filter
        rarities_set = set()
        # Returns the character's alignment with the first letter in uppercase
        charc_alignment = character.charc_alignment()
        charc_alignment = charc_alignment.capitalize()
        # Card data for each user card so the correct data can be displayed
        card_data = {
            "usercard": char,
            "chardetails": character,
            "json": character.get_legends_data(),
            "power": character.power_status(),
            "alignment": charc_alignment,
            "universe": character.charc_universe(),
            "rarity": character.rarity.name,
            "affiliation": character.group_affiliation()
        }
        user_chars.append(card_data)
        rarities_set.add(character.rarity.name)
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

    context = {
        "characters": user_chars,
        "rarities": rarities_set,
        "alignments": sorted(alignments),
        "universes": sorted(universes)
    }
    return render(request, page_url, context)
