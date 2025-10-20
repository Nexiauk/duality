from django.shortcuts import render
import json
import random

def home_view(request):
    page_url = "core/index.html"
    with open("legends.json") as json_file:
        json_data=json.load(json_file)
        res = random.sample(json_data,12)
    context = {
        "characters": res
    }
    print(res)
    return render(request, page_url,context)
