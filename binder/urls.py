"""
URL configuration for the core app
Defines URL patterns for the home view
"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.binder_view, name="binder"),

]
