"""
Signal handlers for automatically creating or updating UserProfile instances
when a Django User is created or saved.

Ensures that every User has an associated UserProfile with default values.
"""
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile
from django.db import transaction


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.get_or_create(
            user=instance,
            defaults={'display_name': instance.username}
        )
    else:
        UserProfile.objects.get_or_create(user=instance)
