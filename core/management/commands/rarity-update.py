"""
Custom management command to update characters
in the CharacterCard model with a rarity from the
Rarity model.
"""
from django.core.management.base import BaseCommand
from django.db import IntegrityError
from pathlib import Path
from core.models import CharacterCard, Rarity
import json


class Command(BaseCommand):
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
                            f"Character with ID{id} was not allocated a rarity. name didn't match")

                except CharacterCard.DoesNotExist:
                    print(f"Character with ID{id} not found")
