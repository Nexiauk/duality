from django.shortcuts import render
from core.models import CharacterCard
import random
from core.data import datastore


def shop_view(request):
    page_url = "shop/shop.html"
    final_list = []
    characters = CharacterCard.objects.all()
    char_list = list(characters)
    res = random.sample(char_list, 12)
    for char in res:
        char_id = char.id
        for item in datastore.legends:
            id = item["id"]
            if id == char_id:
                total_power = sum(item["powerstats"].values())
                pair = {
                    "model": char,
                    "json": item,
                    "power": total_power
                }
                final_list.append(pair)

    context = {
        "characters":final_list
        
    }
    return render(request, page_url, context)
