"""
Defines the UserProfile model and integrates it with Django's
built-in User model.

- Stores additional profile information for users, including a display_name.
- Provides a string representation prioritizing display_name over username.
- Adds a get_display_name property to both UserProfile and User.
  safely falling back to the username if a profile does not exist.
"""


from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class UserProfile(models.Model):
    """
    Stores profile information for a user in the Fableseed app.
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='userprofile'
    )
    display_name = models.CharField(max_length=70)

    def __str__(self):
        """
        Return a string representation of the user profile.
        Uses display_name if available, otherwise falls back to the username.
        """
        return self.display_name if self.display_name else self.user.username

    @property
    def get_display_name(self):
        """
        Provides the display name of the user.
        If the UserProfile does not exist, returns the username.
        """
        try:
            return self.userprofile.display_name
        except User.userprofile.RelatedObjectDoesNotExist:
            return self.username


User.add_to_class(
    'get_display_name',
    UserProfile.get_display_name
)
