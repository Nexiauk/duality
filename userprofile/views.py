"""
Views for the userprofile app.
Renders a profile view and an edit-profile view.
"""
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from userprofile.forms import UserProfileForm, UserForm
from .models import UserProfile


def profile_view(request, id):
    """
    Display a user's profile in read-only mode.
    Renders the profile and user forms with all fields disabled.
    """
    user = get_object_or_404(User, pk=id)
    page_url = "userprofile/view-profile.html"
    try:
        profile = user.userprofile
    except User.userprofile.RelatedObjectDoesNotExist:
        profile = UserProfile(user=user)
    profileform = UserProfileForm(instance=profile)
    userform = UserForm(instance=user)
    for form in [profileform, userform]:
        for field in form.fields.values():
            field.disabled = True
    context = {
        "profile_user": user,
        "profileform": profileform,
        "userform": userform
    }
    return render(request, page_url, context)


@login_required
def edit_profile_view(request, id):
    """
    Allow the logged-in user to edit their profile and account details.
    Handles form submission, validation, saving, and displays
    success or error messages.
    """
    user = get_object_or_404(User, pk=id)
    try:
        profile = user.userprofile
    except User.userprofile.RelatedObjectDoesNotExist:
        profile = UserProfile(user=user)
    page_url = 'userprofile/edit-profile.html'
    if request.method == "POST":
        profileform = UserProfileForm(
            request.POST or None,
            instance=profile
        )
        userform = UserForm(
            request.POST or None,
            instance=user
        )
        if profileform.is_valid() and userform.is_valid():
            userform.save()
            profileform.save()
            if profile.pk is None:
                profile.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "User details successfully updated!"
            )
            return redirect(
                "profile",
                user.pk
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                "Error updating user profile, try again."
            )
    else:
        profileform = UserProfileForm(instance=profile)
        userform = UserForm(instance=user)
    return render(
        request,
        page_url,
        {"profileform": profileform,
         "userform": userform,
         "profile_user": user}
    )
