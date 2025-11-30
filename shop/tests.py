"""
Unit tests for the shop app templates.

Includes:
- Template rendering tests for the shop page.
- Sample CharacterCard, Archetype, and Rarity instances set up for testing.
"""

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from datetime import datetime, timedelta
from core.models import CharacterCard, Archetype, Rarity
from shop.models import ShopScheduler, ShopScheduleItems


class ShopTemplatesViewTests(TestCase):
    """
    Tests for rendering the shop page template with sample characters
    required by the view.
    """

    def setUp(self):
        """Create sample Archetype, Rarity, and CharacterCard instances
          for shop tests."""
        self.hero = Archetype.objects.create(
            literary_archetype="Hero",
            archetype_traits="Heroic"
        )
        self.rarity = Rarity.objects.create(
            name="Uber Awesome",
            level="6",
            price=0.00
        )

        CharacterCard.objects.create(
            id=900,
            name="Lucy",
            can_participate_in_rotation=True,
            archetype=self.hero,
            rarity=self.rarity
        )

        CharacterCard.objects.create(
            id=901,
            name="Luc",
            can_participate_in_rotation=False,
            archetype=self.hero,
            rarity=self.rarity
        )

        CharacterCard.objects.create(
            id=902,
            name="Luca",
            can_participate_in_rotation=True,
            archetype=self.hero,
            rarity=self.rarity
        )

    def test_shop_page_loads_successfully(self):
        """Check that the shop page renders correctly with expected content."""
        response = self.client.get(reverse("shop"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "shop/shop.html")
        self.assertContains(response, "Test Content")

class BaseModelTests(TestCase):
    def setUp(self):
        """Create sample character, with an archetype and rarity, to use as
        as a schedule item in a scheduler instance"""
        self.scheduler = ShopScheduler.objects.create(
            start_time = timezone.make_aware(datetime(2025,10,31,19,00)),
            end_time = timezone.make_aware(datetime(2025,11,1,19,00)),
            rotation_type = "Halloween"
        )
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
        self.schedule_items = ShopScheduleItems.objects.create(
            shop_scheduler = self.scheduler,
            character = self.character_card1,
            sale_price = 0.00
        )

class ShopSchedulerModelTest(BaseModelTests):
    def test_scheduler_start_time(self):
        """Check that the Shop Scheduler has a start time and is correct"""
        self.assertEqual(self.scheduler.start_time, timezone.make_aware(datetime(2025,10,31,19,00)) )

    def test_scheduler_end_time(self):
        """Check that the Shop Scheduler has an end time and is correct"""
        self.assertEqual(self.scheduler.end_time, timezone.make_aware(datetime(2025,11,1,19,00)))

    def test_rotation_type_works(self):
        """Check that the Shop Scheduler has a rotation type"""
        self.assertEqual(self.scheduler.rotation_type, "Halloween")

class ShopScheduleItemsModelTest(BaseModelTests):
    """Check that the schedule item is the correct character"""
    def test_item_includes_character(self):
        self.assertEqual(self.schedule_items.character, self.character_card1)