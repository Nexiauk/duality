"""
This module contains Django models for the core app.
Defines character information, used across the shop and binder apps.
Links those characters to rarities, used to calculate prices,
and archetypes, used for literary references.
"""
from django.db import models
from django.utils.translation import gettext_lazy as _


class CharacterCard(models.Model):
    """
    Represents different characters/legends.
    Base data kept in the database.
    Extended data kept in a JSON file.
    Character information used on cards in the shop and
    binder apps.

    Meta:
        Ordering ascending by name.
        verbose_name: Singular name of the model.
        verbose_name_plural: Plural name of the model
    """
    id = models.IntegerField(primary_key=True)
    name = models.CharField(_("Character Name"), max_length=50)
    can_participate_in_rotation = models.BooleanField(
        _("Can participate in shop rotations"), default=True
    )
    archetype = models.ForeignKey("core.Archetype", verbose_name=_(
        "Archetype"), on_delete=models.PROTECT)

    rarity = models.ForeignKey(
        "core.Rarity",
        verbose_name=_("Rarity"),
        on_delete=models.PROTECT,
        null=True
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Character"
        verbose_name_plural = "Characters"

    def __str__(self):
        """Returns the character's name as its string representation"""
        return self.name


class Archetype(models.Model):
    """
    Represents literary archetypes and
    traits linked to each character in the
    CharacterCards model.

    Meta:
        Orders ascending by literary_archetype
        verbose_name: Singular name of the model.
        verbose_name_plural: Plural name of the model
    """
    literary_archetype = models.CharField(
        _("Literary Archetype"),
        max_length=150
    )
    archetype_traits = models.TextField(_("Archetype Traits"))

    class Meta:
        ordering = ["id"]
        verbose_name = "Archetype"
        verbose_name_plural = "Archetypes"

    def __str__(self):
        """Returns the archetype as its string representation"""
        return self.literary_archetype


class Rarity(models.Model):
    """
    Represents character card rarities.
    Rarity is determined by the totalled power stats of a character.
    It influences the price of cards in the shop and affects styling.

    Meta:
        Ordered by rarity level descending
        verbose_name: Singular name of the model.
        verbose_name_plural: Plural name of the model
    """
    name = models.CharField(_("Rarity Name"), max_length=50)
    level = models.PositiveIntegerField(
        _("Rarity Level")
    )
    price = models.DecimalField(
        _("Price by Rarity"),
        max_digits=5,
        decimal_places=2
        )

    class Meta:
        ordering = ["-level"]
        verbose_name = "Rarity"
        verbose_name_plural = "Rarities"

    def __str__(self):
        """Returns the rarity as its string representation"""
        return self.name
