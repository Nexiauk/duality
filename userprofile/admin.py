from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile
from binder.models import Usercards


class UserProfileInline(admin.StackedInline):
    """
    Inline admin configuration for the UserProfile model.
    Used within the User admin interface to display and edit profiles.
    """
    model = UserProfile
    can_delete = False
    verbose_name_plural = "Profile"
    fk_name = "user"


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
    inlines = (
        UserProfileInline,
        UserCardsInline
        )
    list_display = [
        "userprofile__display_name",
        "username",
        "email",
        "is_staff",
    ]


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
