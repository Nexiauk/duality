"""
Views for the userprofile app.
Renders a profile view and an edit-profile view.
"""
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from userprofile.forms import UserProfileForm, UserForm


def profile_view(request, id):
    user = get_object_or_404(User, pk=id)
    page_url = "userprofile/view-profile.html"
    profile=request.user.userprofile
    profileform = UserProfileForm(instance=profile)
    userform = UserForm(instance=request.user)
    for form in [profileform, userform]:
        for field in form.fields.values():
            field.disabled=True
    context = {
        "user": user,
        "profileform": profileform,
        "userform": userform
    }
    return render(request, page_url, context)


@login_required
def edit_profile_view(request):
    profile = request.user.userprofile
    page_url = 'userprofile/edit-profile.html'

    if request.method == "POST":
        profileform = UserProfileForm(
            request.POST,
            instance=profile
        )
        userform = UserForm(
            request.POST,
            instance=request.user
        )
        if profileform.is_valid() and userform.is_valid():
            userform.save()
            profileform.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "User details successfully updated!"
            )
            return redirect(
                "profile",
                request.user.pk
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                "Error updating user profile, try again."
            )
    else:
        profileform = UserProfileForm(instance=profile)
        userform = UserForm(instance=request.user)
    return render(
        request,
        page_url,
        {"profileform": profileform,
         "userform": userform}
    )
