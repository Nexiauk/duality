from django.test import TestCase
from django.contrib.auth.models import User
from core.models import CharacterCard, Archetype, Rarity
from .models import Usercards
from django.utils import timezone
from datetime import datetime


class BaseModelTests(TestCase):
    def setUp(self):
        """Setup to test the Usercard model. Creates:
        - sample character, with an archetype and rarity
        - test user
        - sample usercard"""
        self.archetype1 = Archetype.objects.create(
            literary_archetype="The Wise Mentor",
            archetype_traits="Wise, nurturing, patient"
        )
        self.rarity_mythic = Rarity.objects.create(
            name="Mythic",
            level=5,
            price=29.99
        )
        self.character_card1 = CharacterCard.objects.create(
            id=1,
            name="Iron Man",
            can_participate_in_rotation=True,
            archetype=self.archetype1,
            rarity=self.rarity_mythic
        )
        self.user = User.objects.create_user(
            username='testuser',
            password='12345'
        )

        self.usercard = Usercards.objects.create(
            owner=self.user,
            character=self.character_card1,
            purchase_price=self.character_card1.rarity.price
        )


class UsercardsModelTest(BaseModelTests):
    """Tests the Usercards model base configuration"""
    def test_stripe_payment_id_auto_created(self):
        """Tests that a stripe payment id is automatically created """
        self.assertIsNotNone(self.usercard.stripe_payment_id)

    def test_order_ref_auto_created(self):
        """Tests that an order reference is automatically
        generated when a usercard is created"""
        self.assertIsNotNone(self.usercard.order_reference)

    def test_owner_matches_user(self):
        """Test that the card owner matches the user"""
        self.assertEqual(self.usercard.owner, self.user)

    def test_character_is_correct(self):
        """Test that the card record matches the purchased character"""
        self.assertEqual(self.usercard.character, self.character_card1)

    def test_purchase_price_is_correct(self):
        """Test that the purchase price matches the character rarity price"""
        self.assertEqual(
            self.usercard.purchase_price,
            self.character_card1.rarity.price
            )

    def test_date_purchased_auto_added(self):
        """Test that the date and time of the usercard creations
        gets automatically added"""
        self.assertIsNotNone(self.usercard.date_purchased)

    def test_verbose_name_works(self):
        """Test that the singular verbose name works"""
        verbose_name = self.usercard._meta.verbose_name
        self.assertEqual(verbose_name, "Usercards")

    def test_verbose_name_plural_works(self):
        """Test that the plural verbose name works"""
        verbose_plural = self.usercard._meta.verbose_name_plural
        self.assertEqual(verbose_plural, "Usercards")

    def test_string_method_works(self):
        """Test that the string method returns the owner's username"""
        self.assertEqual(
            self.usercard.__str__(),
            self.usercard.owner.username
        )

    def test_character_name_returns_correctly(self):
        """Test that the character name method returns the correct
        name from the associated character card"""
        self.assertEqual(
            self.usercard.character_name(),
            "Iron Man"
        )

    def test_order_ref_generates_correctly(self):
        """Test that the order reference method returns
        the correct configuration of character name, id number
        and a zfill of 4"""
        self.assertEqual(
            self.usercard.order_ref(),
            "IRON0001"
        )
