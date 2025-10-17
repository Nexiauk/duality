"""
This module contains Django models for the core app.
Defines character information, used across the shop and binder apps.
Links those characters to rarities, used to calculate prices,
and archetypes, used for literary references.
"""

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class CharacterCards(models.Model):
    """
    Represents different characters that
    are used across the shop and binder apps.

    Meta:
        Ordering ascending by name.
        verbose_name: Singular name of the model.
        verbose_name_plural: Plural name of the model
    """
    name = models.CharField(_("Character Name"), max_length=50)
    can_participate_in_rotation = models.BooleanField(
        _("Can participate in shop rotations"), default=True
    )
    archetype = models.ForeignKey("core.Archetype", verbose_name=_(
        "Archetype"), on_delete=models.PROTECT)

    rarity = models.ForeignKey(
        "core.Rarity", verbose_name=_("Rarity"), on_delete=models.PROTECT)
    
    class Meta:
        ordering = ["name"]
        verbose_name = "Character"
        verbose_name_plural = "Characters"
