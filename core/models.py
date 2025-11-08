"""
This module contains Django models for the core app.
Defines character information, used across the shop and binder apps.
Links those characters to rarities, used to calculate prices,
and archetypes, used for literary references.
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from core.data import datastore


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
        null=False
    )

    def get_legends_data(self):
        char_id = self.character.id
        legend = next((item for item in datastore.legends if item["id"] == char_id), None)
        return legend
    
    def power_status(self):
        legend_data = self.get_legends_data()
        total_power = sum(legend_data["powerstats"].values())
        return total_power

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
        ordering = ["literary_archetype"]
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
    name = models.CharField(_("Rarity Name"), max_length=50, unique=True)
    # Numeric representation of rarity used for algorithmic calculations.
    # Lower values indicate more common items;
    # Higher values are rarer and less frequent.
    level = models.PositiveIntegerField(
        _("Rarity Level"),
        unique=True,
        help_text="Numeric rarity level used for algorithmic calculations. "
        "Lower numbers are more common; higher numbers are rarer."
    )
    price = models.DecimalField(
        _("Price by Rarity"),
        max_digits=5,
        decimal_places=2,
        null=False
    )

    class Meta:
        ordering = ["-level"]
        verbose_name = "Rarity"
        verbose_name_plural = "Rarities"

    def __str__(self):
        """Returns the rarity as its string representation"""
        return self.name
