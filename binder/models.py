"""
Models for the binder app.

Defines user card records used to track purchases, including
built-in handling for deleted users to preserve purchase
history.
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from core.models import CharacterCard
from decimal import Decimal


class Usercards(models.Model):
    """
    Represents a usercard record for a single purchase.

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
        max_digits=5,
        decimal_places=2,
        null=False,
        verbose_name=_("Purchase Price")
        )

    class Meta:
        """
        Constraint added so an owner cannot have more than
        one UserCard for the same character.
        """
        verbose_name = _("Usercards")
        verbose_name_plural = _("Usercards")
        ordering = ["-date_purchased"]
        constraints = [
            models.UniqueConstraint(
                fields=['owner', 'character'],
                name='unique_owner_character_pair'
            )
        ]

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
        """
        Return the name of the associated character.
        """
        return self.character.name

    def order_ref(self):
        """
        Generate a unique order reference combining the first significant
        word of the character's name and the usercard ID, zero-padded.
        """
        ignore_list = {'the', 'a', 'an'}
        split = self.character.name.split()
        for word in split:
            if word.upper() not in ignore_list:
                first_word = word.upper()
                break
        string = str(self.id)
        order_number = first_word + string.zfill(4)
        return order_number

    @classmethod
    def create_usercard(cls, user, purchase, payment_intent):
        """
        Create or retrieve a Usercard for a given user and purchase.

        Records the character, purchase price, and Stripe payment ID.
        Generates and saves an order reference if not already set.
        Returns the Usercard instance.
        """
        character = CharacterCard.objects.get(id=purchase['character_id'])
        price_in_pounds = Decimal(purchase['price']) / 100
        usercard, created = cls.objects.get_or_create(
            owner=user,
            stripe_payment_id=payment_intent,
            character=character,
            defaults={
                'purchase_price': price_in_pounds
            }
        )
        if created or not usercard.order_ref:
            usercard.order_reference = usercard.order_ref()
            usercard.save(update_fields=['order_reference'])
        return usercard
