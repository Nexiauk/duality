from django.shortcuts import render
from pathlib import Path
import json
import random

def home_view(request):
    page_url = "core/index.html"
    FILE_PATH = Path(__file__).parent/"data"/"legends.json"
    with open(FILE_PATH, "r", encoding="utf-8") as json_file:
        json_data=json.load(json_file)
        res = random.sample(json_data,12)
    context = {
        "characters": res
    }
    print(res)
    return render(request, page_url,context)
