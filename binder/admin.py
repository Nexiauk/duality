"""
Admin configuration for the core app models.

This module customises the Django admin interface for the
Binder model: UserCards.
"""
from django.contrib import admin
from .models import Usercards
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


@admin.register(Usercards)
class UserCardsAdmin(admin.ModelAdmin):
    """Custom admin configuration for user cards allowing admin to see all
    purchases by all users in one central location. Includes Filters for date
    and price, and is searchable by order reference number and stripe
    payment reference"""
    list_display = (
        "character_name",
        "id",
        "owner",
        "order_reference",
        "stripe_payment_id",
        "date_purchased",
        "purchase_price"
    )

    list_filter = ("date_purchased", "purchase_price",)
    search_fields = ["order_reference", "stripe_payment_id", "character__name"]
