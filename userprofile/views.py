"""
Views for the core app.
Renders index.html
"""
from django.shortcuts import render


def profile_view(request):
    page_url = "userprofile/view-profile.html"
    return render(request, page_url)
