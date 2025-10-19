from django.shortcuts import render
import json

def home_view(request):
    page_url = "core/index.html"
    with open("731_legends_with_archetypes.json") as json_file:
        json_data=json.load(json_file)
    context = {
        "characters":json_data
    }
    return render(request, page_url,context)
