from django.shortcuts import render
from pathlib import Path
from .models import CharacterCard
import random
import json
from core.data import datastore


def home_view(request):
    page_url = "core/index.html"
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
    print(res)
    return render(request, page_url, context)
