"""
Forms for user registration and profile management.

Includes:
- CustomSignupForm: Extends allauth's SignupForm to add a display_name field.
- UserProfileForm: ModelForm for editing the UserProfile.
- UserForm: ModelForm for editing basic User fields.
"""
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm
from django import forms
from .models import UserProfile


class CustomSignupForm(SignupForm):
    """
    Custom signup form that extends allauth's SignupForm to include
    a 'display_name' field and save it to the associated UserProfile.
    """
    display_name = forms.CharField(max_length=70, label="Display Name")

    def save(self, request):
        """
        Save the user and assign the display_name to the related UserProfile.
        """
        user = super().save(request)

        profile, created = UserProfile.objects.get_or_create(
            user=user,
            defaults={'display_name': self.cleaned_data["display_name"]}
        )
        if not created:
            user.userprofile.display_name = self.cleaned_data["display_name"]
            user.userprofile.save()
        return user


class UserProfileForm(forms.ModelForm):
    """
    Signup form extending allauth's SignupForm to include a display_name field
    and save it to the associated UserProfile.
    """
    prefix = "profiledata"

    class Meta:
        model = UserProfile
        fields = ["display_name"]


class UserForm(forms.ModelForm):
    """
    Form for editing basic user information: first name, last name, and email.
    """
    prefix = "userdata"

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
