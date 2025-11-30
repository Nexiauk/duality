"""
Admin configuration for the core app models.

This module customises the Django admin interface for the
Binder model: UserCards.
"""
from django.contrib import admin
from .models import Usercards


@admin.register(Usercards)
class UserCardsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "owner",
        "character_name",
        "order_reference",
        "date_purchased",
        "purchase_price"
    )
