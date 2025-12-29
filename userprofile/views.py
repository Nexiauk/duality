"""
Views for the userprofile app.
Renders a profile view and an edit-profile view.
"""
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from userprofile.forms import UserProfileForm


def profile_view(request, id):
    user = get_object_or_404(User, pk=id)
    page_url = "userprofile/view-profile.html"
    context = {
        "user": user
    }
    return render(request, page_url, context)


@login_required
def edit_profile_view(request):
    profile = request.user.userprofile
    page_url = 'userprofile/edit-profile.html'

    if request.method == "POST":
        form = UserProfileForm(
            request.POST,
            instance=profile
        )
        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Profile successfully updated!"
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
        form = UserProfileForm(instance=profile)
    return render(
        request,
        page_url,
        {"form": form}
    )
