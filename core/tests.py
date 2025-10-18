from django.test import TestCase
from django.urls import reverse
from core.models import CharacterCard, Archetype, Rarity

class CoreTemplatesViewTests(TestCase):
    def test_index_page_loads_successfully(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/index.html")
        self.assertContains(response, "Test content")
        
class BaseModelTest(TestCase):
    def setUp(self):
        self.archetype1 = Archetype.objects.create(
            literary_archetype = "The Wise Mentor",
            archetype_traits = "Wise, nurturing, patient"
        )

        self.archetype2 = Archetype.objects.create(
            literary_archetype = "The Trickster",
            archetype_traits = "Mysterious, alluring, inconsistent"
        )

        self.rarity_mythic = Rarity.objects.create(
            name = "Mythic",
            level = 5,
            price = 29.99
        )

        self.rarity_common = Rarity.objects.create(
            name = "Common",
            level = 1,
            price = 0
        )

        self.character_card1 = CharacterCard.objects.create(
            name = "Iron Man",
            can_participate_in_rotation = True,
            archetype = self.archetype1,
            rarity = self.rarity_mythic
        )
        self.character_card2 = CharacterCard.objects.create(
            name = "Ant Man",
            can_participate_in_rotation = False,
            archetype = self.archetype2,
            rarity = self.rarity_common
        )

class CharacterCardModelTests(BaseModelTest):
    def test_verbose_name_for_character_card_model_works(self):
        verbose_name = self.character_card._meta.verbose_name
        self.assertEqual(verbose_name, "Character")
        
    def test_verbose_name_plural_for_character_card_model_works(self):
        plural_name = self.character_card._meta.verbose_name_plural
        self.assertEqual(plural_name, "Characters")

    def test_character_name_created_correctly(self):
        self.assertEqual(self.character_card1.name, "Iron Man")
    
    def test_rotation_boolean_works(self):
        self.assertTrue(self.character_card1.can_participate_in_rotation)

    def test_character_has_correct_archetype(self):
        self.assertEqual(self.character_card1.archetype, self.archetype1)

    def test_character_archetype_name(self):
        self.assertEqual(self.character_card1.archetype.literary_archetype, "The Wise Mentor")

    def test_character_has_rarity(self):
        self.assertEqual(self.character_card1.rarity, self.rarity_mythic)

    def test_character_rarity_name(self):
        self.assertEqual(self.character_card1.rarity.name, "Mythic")

class RarityModelTests(BaseModelTest):
    def test_rarity_name(self):
        self.assertEqual(self.rarity_mythic.name, "Mythic")

    def test_rarity_has_level(self):
        self.assertEqual(self.rarity_mythic.level, 5)

    def test_rarity_price(self):
        self.assertEqual(self.rarity_mythic.price, 29.99)

    def test_verbose_name_singular_for_rarity_model(self):
        verbose_name = self.rarity_mythic._meta.verbose_name
        self.assertEqual(verbose_name, "Rarity")

    def test_verbose_name_plural_for_rarity_model(self):
        verbose_name = self.rarity_mythic._meta.verbose_name_plural
        self.assertEqual(verbose_name, "Rarities")

    def test_rarity_ordering_works(self):
        all_rarities = list(Rarity.objects.all())
        expected_order = [self.rarity_mythic, self.rarity_common]
        self.assertEqual(all_rarities, expected_order)
