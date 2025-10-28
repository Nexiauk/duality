from django.shortcuts import render
from core.models import CharacterCard
import random
from core.data import datastore


def shop_view(request):
    page_url = "shop/shop.html"
    final_list = []
    characters = CharacterCard.objects.all()
    char_list = list(characters)
    res = random.sample(char_list, 3)
    for char in res:
        char_id = char.id
        for item in datastore.legends:
            id = item["id"]
            if id == char_id:
                pair = {
                    "model": char,
                    "json": item
                }
                final_list.append(pair)

    context = {
        "characters":final_list
        
    }
    return render(request, page_url, context)
