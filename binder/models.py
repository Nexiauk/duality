from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from core.models import CharacterCard
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.


class Usercards(models.Model):
    stripe_payment_id = models.CharField(
        _("Stripe Payment Reference"),
        max_length=300
    )
    payment_reference = models.CharField(
        _("Order Reference Number"),
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
        if self.owner is not None:
            return self.owner.username
        else:
            return "Deleted user"
