"""
Unit tests for the shop app templates.

Includes:
- Template rendering tests for the shop page.
- Sample CharacterCard, Archetype, and Rarity instances set up for testing.
"""

from django.test import TestCase
from django.urls import reverse
from core.models import CharacterCard, Archetype, Rarity


class ShopTemplatesViewTests(TestCase):
    """Tests for rendering the shop page template with sample characters."""

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
