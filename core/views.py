"""
Views for the core app.
Renders index.html
"""
from django.shortcuts import render


def home_view(request):
    page_url = "core/index.html"
    return render(request, page_url)
