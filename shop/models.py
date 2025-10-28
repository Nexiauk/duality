"""
This module contains Django models for the shop app.
Defines the Shop Scheduler and the items assigned to each schedule.
"""
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from decimal import Decimal, ROUND_HALF_UP
from datetime import timedelta


class ShopScheduler(models.Model):
    start_time = models.DateTimeField(_("Start Time"))
    end_time = models.DateTimeField(_("End Time"))
    rotation_type = models.CharField(_("Rotation Type"), max_length=150)

    def save(self, *args, **kwargs):
        if not self.start_time:
            self.start_time = timezone.now()
        if not self.end_time:
            self.end_time = self.start_time + timedelta(hours=24)
        super().save(*args, **kwargs)

class ShopScheduleItems(models.Model):
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
    @property
    def active_price(self):
        price = self.sale_price if self.sale_price is not None else self.character.rarity.price
        formatted_price = price.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        return f"£{formatted_price}"
    
