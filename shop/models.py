"""
This module contains Django models for the shop app.
Defines shop schedules and the items assigned to each schedule,
including sale pricing and automatic end-time calculation.
"""

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from decimal import Decimal, ROUND_HALF_UP


class ShopScheduler(models.Model):
    """
    Represents a shop schedule, defining a start and end time
    and the type of rotation (e.g., daily, weekly).
    """
    start_time = models.DateTimeField(_("Start Time"))
    end_time = models.DateTimeField(_("End Time"))
    rotation_type = models.CharField(_("Rotation Type"), max_length=150, default="Daily")

    class Meta:
        ordering = ["start_time"]
        verbose_name = "Shop Scheduler"
        verbose_name_plural = "Shop Scheduler"

    def __str__(self):
        if self.rotation_type:
            return (
                f"{self.rotation_type} "
                f"({self.start_time.date()} → "
                f"{self.end_time.date()})"
            )


class ShopScheduleItems(models.Model):
    """
    Represents an item (character card) assigned to a shop schedule.

    Properties:
        active_price (str): Returns the effective price for the item as a
                            formatted string with a currency symbol.
                            Uses sale_price if set, otherwise falls back
                            to the character's rarity price.
    """
    shop_scheduler = models.ForeignKey(
        "shop.ShopScheduler",
        verbose_name=_("Shop Scheduler"),
        on_delete=models.CASCADE
    )
    character = models.ForeignKey(
        "core.CharacterCard",
        verbose_name=_("Character"),
        on_delete=models.CASCADE
    )
    sale_price = models.DecimalField(
        _("Sale Price"),
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ["shop_scheduler"]
        verbose_name = "Schedule Items"
        verbose_name_plural = "Schedule Items"


    def __str__(self):
        return (
            f"{self.character.name} in "
            f"{self.shop_scheduler} – "
            f"{self.active_price}"
        )

    @property
    def active_price(self):
        """
        Returns the active price for the item as a formatted string
        with a currency symbol.

        Logic:
            - Use sale_price if it is set.
            - Otherwise, fall back to the character's rarity price.
            - Ensures two decimal places with proper rounding.

        Returns:
            Price formatted as '£XX.XX'.
        """
        price = (
            self.sale_price
            if self.sale_price is not None
            else self.character.rarity.price
        )
        formatted_price = price.quantize(
            Decimal("0.01"),
            rounding=ROUND_HALF_UP
        )
        return f"£{formatted_price}"
