"""
URL configuration for the userprofile app
Defines URL patterns for the profile view
"""

from django.urls import path
from . import views

urlpatterns = [
    path("view-profile/<int:id>/", views.profile_view, name="profile"),
    path("edit-profile/", views.edit_profile_view, name="edit-profile"),

]
