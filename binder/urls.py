"""
URL configuration for the Binder app
Defines URL patterns for the binder view
"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.binder_view, name="binder"),

]
