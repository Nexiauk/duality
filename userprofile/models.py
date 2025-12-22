from django.db import models
from django.contrib.auth.models import User


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
        except UserProfile.DoesNotExist:
            return self.username


User.add_to_class(
    'get_display_name',
    UserProfile.get_display_name
)
