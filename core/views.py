from django.shortcuts import render
from .models import CharacterCard
import random
from core.data import datastore


def home_view(request):
    page_url = "core/index.html"
    return render(request, page_url)
