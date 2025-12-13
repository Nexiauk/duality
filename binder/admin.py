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
    list_display = (
        "id",
        "owner",
        "character_name",
        "order_reference",
        "stripe_payment_id",
        "date_purchased",
        "purchase_price"
    )


class UserCardsInline(admin.TabularInline):
    """
    An inline admin configuration, to show
    usercards inline with user records.
    """
    model = Usercards
    extra = 0
    fields = (
        "order_reference",
        "stripe_payment_id",
        "character",
        "date_purchased",
        "purchase_price",

              )
    readonly_fields = (
        "order_reference",
        "stripe_payment_id",
        "date_purchased",
        "purchase_price",
    )


class CustomUserAdmin(UserAdmin):
    """
    Custom admin configuration for the User model.
    Includes the UserProfile inline and custom list display.
    """
    inlines = (UserCardsInline,)
    list_display = [
        "username",
        "email",
        "is_staff",
    ]


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
