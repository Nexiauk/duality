"""
Models for the shop app.

Defines shop schedules and their associated items.
Schedules control rotation timing and determine which
characters are available in the shop.
"""

from django.db import models, IntegrityError
from django.utils import timezone
from django.utils.timezone import timedelta
from django.utils.translation import gettext_lazy as _
from decimal import Decimal, ROUND_HALF_UP
from core.models import CharacterCard
import random


def start_time_default():
    """Returns the default start time (current time)."""
    return timezone.now()


def end_time_default():
    """Returns the default end time (24 hours from now)."""
    return timezone.now()+timedelta(hours=24)


class ShopScheduler(models.Model):
    """
    Represents a shop schedule, defining a start and end time
    and the type of rotation (e.g., daily, weekly).
    """
    start_time = models.DateTimeField(
        _("Start Time"),
        default=start_time_default
        )
    end_time = models.DateTimeField(
        _("End Time"),
        default=end_time_default
        )
    rotation_type = models.CharField(
        _("Rotation Type"),
        max_length=150,
        default="Daily"
        )
    characters = models.ManyToManyField(
        "core.CharacterCard",
        through="shop.ShopScheduleItems",
        through_fields=("shop_scheduler", "character"),
        related_name="shop_schedules",
        blank=True,
    )

    @classmethod
    def currently_active_schedules(cls):
        """Returns all schedules active at the current time."""
        now = timezone.now()
        active_schedules = cls.objects.filter(
            start_time__lte=now,
            end_time__gte=now
        )
        return active_schedules

    @classmethod
    def get_or_create_active_schedule(cls):
        """
        Returns the current active schedule(s),
        or creates a new one if none exist.
        """
        active_schedules = ShopScheduler.currently_active_schedules()
        if active_schedules.exists():
            return active_schedules
        try:
            new_schedule = ShopScheduler.objects.create(
                start_time=start_time_default(),
                end_time=end_time_default(),
                rotation_type="Daily"
            )
            return [new_schedule]
        except IntegrityError:
            return cls.currently_active_schedules

    def get_items(self):
        """Returns all characters assigned to this schedule."""
        characters = [item.character for item in self.scheduled_items.all()]
        return characters

    def get_eligible_characters(self):
        """Returns characters in the schedule
        that can participate in rotation."""
        eligible_characters = []
        characters = self.get_items()
        for char in characters:
            if char.can_participate_in_rotation:
                eligible_characters.append(char)
        return eligible_characters

    def create_items_for_schedule(self):
        """Randomly assigns 12 characters to this schedule."""
        characters = CharacterCard.objects.filter(
            can_participate_in_rotation=True
            )
        char_list = list(characters)
        sampled_characters = random.sample(char_list, 12)
        for char in sampled_characters:
            ShopScheduleItems.objects.create(
                shop_scheduler=self,
                character=char,
                sale_price=0
            )

    class Meta:
        ordering = ["-start_time"]
        verbose_name = "Shop Scheduler"
        verbose_name_plural = "Shop Scheduler"
        constraints = [
            models.UniqueConstraint(
                fields=["start_time"],
                name="unique_shop_per_start_time"
            )
        ]

    def __str__(self):
        """Returns a string representation of the schedule."""
        if self.rotation_type:
            return (
                f"{self.rotation_type} "
                f"({self.start_time.date()} → "
                f"{self.end_time.date()})"
            )


class ShopScheduleItems(models.Model):
    """
    Represents a character item within a shop schedule,
    optionally discounted with a sale price.
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
        """Returns a string representation of the item."""
        return (
            f"{self.character.name} in "
            f"{self.shop_scheduler} – "
            f"{self.active_price}"
        )

    @property
    def active_price(self):
        """
        Returns the effective price for the item.

        Uses sale_price if set; otherwise, falls back
        to the character's rarity price. Ensures
        rounding to two decimal places.
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
