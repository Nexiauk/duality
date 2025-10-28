"""
Unit tests for core app models and templates.

Includes tests for:
- Template rendering (CoreTemplatesViewTests)
- CharacterCard model (CharacterCardModelTests)
- Rarity model (RarityModelTests)
- Archetype model (ArchetypeModelTests)

Uses BaseModelTest to provide sample instances
for model testing.
"""

from django.test import TestCase
from django.urls import reverse
from core.models import CharacterCard, Archetype, Rarity


class CoreTemplatesViewTests(TestCase):
    """Tests for rendering core app templates."""

    def test_index_page_loads_successfully(self):
        """Check that the home page renders correctly with expected content."""
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/index.html")
        self.assertContains(response, "Test content")


class BaseModelTest(TestCase):
    """Sets up sample model instances for use in other model tests."""

    def setUp(self):
        """Create sample Archetype, Rarity, and CharacterCard instances."""
        self.archetype1 = Archetype.objects.create(
            literary_archetype="The Wise Mentor",
            archetype_traits="Wise, nurturing, patient"
        )
        self.archetype2 = Archetype.objects.create(
            literary_archetype="The Trickster",
            archetype_traits="Mysterious, alluring, inconsistent"
        )
        self.rarity_mythic = Rarity.objects.create(
            name="Mythic",
            level=5,
            price=29.99
        )
        self.rarity_common = Rarity.objects.create(
            name="Common",
            level=1,
            price=0
        )
        self.character_card1 = CharacterCard.objects.create(
            name="Iron Man",
            can_participate_in_rotation=True,
            archetype=self.archetype1,
            rarity=self.rarity_mythic
        )
        self.character_card2 = CharacterCard.objects.create(
            name="Ant Man",
            can_participate_in_rotation=False,
            archetype=self.archetype2,
            rarity=self.rarity_common
        )


class CharacterCardModelTests(BaseModelTest):
    """Tests for the CharacterCard model functionality."""

    def test_verbose_name_for_character_card_model_works(self):
        """Check the singular verbose_name of CharacterCard."""
        verbose_name = self.character_card1._meta.verbose_name
        self.assertEqual(verbose_name, "Character")

    def test_verbose_name_plural_for_character_card_model_works(self):
        """Check the plural verbose_name of CharacterCard."""
        plural_name = self.character_card1._meta.verbose_name_plural
        self.assertEqual(plural_name, "Characters")

    def test_character_name_created_correctly(self):
        """Ensure character name is stored correctly."""
        self.assertEqual(self.character_card1.name, "Iron Man")

    def test_rotation_boolean_works(self):
        """Ensure can_participate_in_rotation boolean is correct."""
        self.assertTrue(self.character_card1.can_participate_in_rotation)

    def test_character_has_correct_archetype(self):
        """Check that character is assigned the correct archetype."""
        self.assertEqual(self.character_card1.archetype, self.archetype1)

    def test_character_archetype_name(self):
        """Check the name of the character's archetype."""
        self.assertEqual(
            self.character_card1.archetype.literary_archetype,
            "The Wise Mentor"
        )

    def test_character_has_rarity(self):
        """Check that character has the correct rarity."""
        self.assertEqual(self.character_card1.rarity, self.rarity_mythic)

    def test_character_rarity_name(self):
        """Check the name of the character's rarity."""
        self.assertEqual(self.character_card1.rarity.name, "Mythic")

    def test_character_ordering_works(self):
        """Verify the default ordering of CharacterCard instances."""
        characters = list(CharacterCard.objects.all())
        expected_order = [self.character_card2, self.character_card1]
        self.assertEqual(characters, expected_order)

    def test_character_string_method(self):
        """Check that __str__ method returns character's name."""
        self.assertEqual(
            self.character_card1.__str__(),
            self.character_card1.name
        )


class RarityModelTests(BaseModelTest):
    """Tests for the Rarity model functionality."""

    def test_rarity_name(self):
        """Check rarity name is stored correctly."""
        self.assertEqual(self.rarity_mythic.name, "Mythic")

    def test_rarity_has_level(self):
        """Check rarity level is stored correctly."""
        self.assertEqual(self.rarity_mythic.level, 5)

    def test_rarity_price(self):
        """Check rarity price is stored correctly."""
        self.assertEqual(self.rarity_mythic.price, 29.99)

    def test_verbose_name_singular_for_rarity_model(self):
        """Check singular verbose_name for Rarity model."""
        verbose_name = self.rarity_mythic._meta.verbose_name
        self.assertEqual(verbose_name, "Rarity")

    def test_verbose_name_plural_for_rarity_model(self):
        """Check plural verbose_name for Rarity model."""
        verbose_name = self.rarity_mythic._meta.verbose_name_plural
        self.assertEqual(verbose_name, "Rarities")

    def test_rarity_ordering_works(self):
        """Verify the default ordering of Rarity instances."""
        all_rarities = list(Rarity.objects.all())
        expected_order = [self.rarity_mythic, self.rarity_common]
        self.assertEqual(all_rarities, expected_order)

    def test_rarity_string_method(self):
        """Check that __str__ method returns rarity's name."""
        self.assertEqual(self.rarity_mythic.__str__(), self.rarity_mythic.name)


class ArchetypeModelTests(BaseModelTest):
    """Tests for the Archetype model functionality."""

    def test_archetype_name(self):
        """Check literary archetype name is stored correctly."""
        self.assertEqual(self.archetype1.literary_archetype, "The Wise Mentor")

    def test_archetype_traits(self):
        """Check archetype traits are stored correctly."""
        self.assertEqual(
            self.archetype1.archetype_traits,
            "Wise, nurturing, patient"
        )

    def test_verbose_name_singular_for_archetype_model(self):
        """Check singular verbose_name for Archetype model."""
        verbose_name = self.archetype1._meta.verbose_name
        self.assertEqual(verbose_name, "Archetype")

    def test_verbose_name_plural_for_archetype_model(self):
        """Check plural verbose_name for Archetype model."""
        verbose_name = self.archetype1._meta.verbose_name_plural
        self.assertEqual(verbose_name, "Archetypes")

    def test_archetype_ordering_works(self):
        """Verify default ordering of Archetype instances."""
        all_archetypes = list(Archetype.objects.all())
        expected_order = [self.archetype2, self.archetype1]
        self.assertEqual(all_archetypes, expected_order)

    def test_archetype_string_method(self):
        """Check that __str__ method returns archetype name."""
        self.assertEqual(
            self.archetype1.__str__(),
            self.archetype1.literary_archetype
        )
