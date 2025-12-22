from allauth.account.forms import SignupForm
from django import forms

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
        user.userprofile.display_name = self.cleaned_data["display_name"]
        user.userprofile.save()
        return user