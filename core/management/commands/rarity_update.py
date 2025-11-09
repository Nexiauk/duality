"""
Custom Django management command to assign a rarity to each character
in the CharacterCard model based on their total power.
"""
from django.core.management.base import BaseCommand
from django.db import IntegrityError
from pathlib import Path
from core.models import CharacterCard, Rarity
import json


class Command(BaseCommand):
    """
The command reads character data from `legends.json` and does the following:

1. Iterates over each character in the JSON file.
2. For each character, retrieves the corresponding CharacterCard record by ID.
3. Checks that the name in the JSON matches the database record.
   - If the name doesn't match, a warning is printed and the record is skipped.
4. Calculates the total power as the sum of all values in the `powerstats`
dictionary.
5. Assigns a rarity based on the total power thresholds:
   - 0–160       → Common
   - 161–260     → Uncommon
   - 261–360     → Rare
   - 361–460     → Epic
   - 461–560     → Legendary
   - 561–660     → Mythic
6. If a CharacterCard with the given ID does not exist, a warning is printed.
"""
    def handle(self, *args, **kwargs):
        file_path = Path(__file__).parent.parent.parent/"data"/"legends.json"
        with open(file_path, "r", encoding="utf-8") as json_file:
            json_data = json.load(json_file)
            for item in json_data:
                id = item["id"]
                json_name = item["name"]
                try:
                    character = CharacterCard.objects.get(id=id)
                    if character.name == json_name:
                        total_power = sum(item["powerstats"].values())
                        if total_power <= 160:
                            CharacterCard.objects.filter(id=id).update(
                                rarity=Rarity.objects.get(name="Common")
                            )
                        elif total_power >= 161 and total_power <= 260:
                            CharacterCard.objects.filter(id=id).update(
                                rarity=Rarity.objects.get(name="Uncommon")
                            )
                        elif total_power >= 261 and total_power <= 360:
                            CharacterCard.objects.filter(id=id).update(
                                rarity=Rarity.objects.get(name="Rare")
                            )
                        elif total_power >= 361 and total_power <= 460:
                            CharacterCard.objects.filter(id=id).update(
                                rarity=Rarity.objects.get(name="Epic")
                            )
                        elif total_power >= 461 and total_power <= 560:
                            CharacterCard.objects.filter(id=id).update(
                                rarity=Rarity.objects.get(name="Legendary")
                            )
                        elif total_power >= 561 and total_power <= 660:
                            CharacterCard.objects.filter(id=id).update(
                                rarity=Rarity.objects.get(name="Mythic")
                            )
                    else:
                        print(
                            f"Character {id} was not allocated a rarity.")

                except CharacterCard.DoesNotExist:
                    print(f"Character with ID{id} not found")
