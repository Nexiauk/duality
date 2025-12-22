from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileInline(admin.StackedInline):
    """
    Inline admin configuration for the UserProfile model.
    Used within the User admin interface to display and edit profiles.
    """
    model = UserProfile
    can_delete = False
    verbose_name_plural = "Profile"
    fk_name = "user"


class CustomUserAdmin(UserAdmin):
    """
    Custom admin configuration for the User model.
    Includes the UserProfile inline and custom list display.
    """
    inlines = (UserProfileInline,)
    list_display = [
        "userprofile__display_name",
        "username",
        "email",
        "is_staff",
    ]


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

