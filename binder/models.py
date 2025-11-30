"""
Models for the binder app.

Defines user card records used to track purchases, including
built-in handling for deleted users to preserve purchase
history.
"""
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from core.models import CharacterCard


class Usercards(models.Model):
    """
    Represents a user card record for a single purchase.

    Stores Stripe payment id and a user-friendly
    order reference, as well as purchase date/time,
    price paid at the time the purchase was made, and links
    to the purchasing user and the character purchased.
    """
    stripe_payment_id = models.CharField(
        verbose_name=_("Stripe Payment Reference"),
        max_length=300
    )
    order_reference = models.CharField(
        verbose_name=_("Order Reference Number"),
        max_length=300
    )
    owner = models.ForeignKey(
        User,
        verbose_name=_("User Name"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    character = models.ForeignKey(
        CharacterCard,
        verbose_name=_("Character Purchased"),
        on_delete=models.PROTECT
    )
    date_purchased = models.DateTimeField(auto_now_add=True)
    purchase_price = models.DecimalField(
        _(""), max_digits=5, decimal_places=2, null=False)

    class Meta:
        verbose_name = _("Usercards")
        verbose_name_plural = _("Usercards")

    def __str__(self):
        """
        Returns the owner's username if the user exists.
        If the user has been deleted, returns "Deleted user".
        """
        if self.owner is not None:
            return self.owner.username
        else:
            return "Deleted user"
        
    def character_name(self):
        return self.character.name
