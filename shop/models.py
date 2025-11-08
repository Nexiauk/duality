"""
This module contains Django models for the shop app.
Defines shop schedules and the items assigned to each schedule,
including sale pricing and automatic end-time calculation.
"""

from django.db import models
from django.utils import timezone
from django.utils.timezone import timedelta
from django.utils.translation import gettext_lazy as _
from decimal import Decimal, ROUND_HALF_UP
from core.models import CharacterCard
import random


class ShopScheduler(models.Model):
    """
    Represents a shop schedule, defining a start and end time
    and the type of rotation (e.g., daily, weekly).
    """
    @staticmethod
    def start_time_default():
        return timezone.now()
    
    @staticmethod
    def end_time_default():
        return timezone.now()+timedelta(hours=24)

    start_time = models.DateTimeField(_("Start Time"), default=start_time_default)
    end_time = models.DateTimeField(_("End Time"), default=end_time_default)
    rotation_type = models.CharField(_("Rotation Type"), max_length=150, default="Daily")

    @classmethod 
    def currently_active_schedules(cls):
        now = timezone.now()
        active_schedules = cls.objects.filter(
        start_time__lte=now,
        end_time__gte=now
    )
        return active_schedules
    
    @classmethod
    def get_or_create_active_schedule(cls):
        active_schedules = ShopScheduler.currently_active_schedules()
        if active_schedules.exists():
            return active_schedules
        else:
            new_schedule = ShopScheduler.objects.create(
                start_time = ShopScheduler.start_time_default(),
                end_time = ShopScheduler.end_time_default(),
                rotation_type = "Daily"
            )
            return [new_schedule]

    
    def get_items(self):
        characters = [item.character for item in self.scheduled_items.all()]
        return characters
    
    def get_eligible_characters(self):
        eligible_characters = []
        characters = self.get_items()
        for char in characters:
            if char.can_participate_in_rotation:
                eligible_characters.append(char)
        return eligible_characters
    
    def create_items_for_schedule(self):
        characters = CharacterCard.objects.all()
        char_list = list(characters)
        sampled_characters = random.sample(char_list, 12)
        for char in sampled_characters:
            ShopScheduleItems.objects.create(
                shop_scheduler = self,
                character = char,
                sale_price = 0
            )

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
        on_delete=models.CASCADE,
        related_name="scheduled_items"
    )
    character = models.ForeignKey(
        "core.CharacterCard",
        verbose_name=_("Character"),
        on_delete=models.CASCADE,
        related_name="scheduled_characters"
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
