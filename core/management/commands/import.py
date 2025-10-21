"""
Custom management command to import character data
from a json file
"""
from django.core.management.base import BaseCommand
from django.db import IntegrityError
from pathlib import Path
from core.models import CharacterCard
import json


class Command(BaseCommand):
    """
    Django management command to import character data from a JSON file.

    Uses 'legends.json' located in the data directory. Maps archetype names
    to their corresponding numeric IDs and creates CharacterCard objects
    for each entry in the JSON.

    Inherits from BaseCommand.
    """

    help = "Imports character objects from legends.json file"

    def handle(self, *args, **kwargs):
        """
        Imports character data from a raw json file into the
        CharacterCard model.
        Reads the JSON file with multiple character objects,
        each with a unique ID and creates corresponding records
        in the CharacterCard table.

        Fields in the json file that don't exist in the Django
        model are ignored.
        The JSON id field is mapped directly to the CharacterCard
        Primary Key.

        An error is raised if the file isn't found, or if rows
        cannot be created in the table.

        Maps archetype string data to existing archetype primary
        keys in the archetype table.
        Maps characters without archetypes to a placeholder
        archetype record.
        """
        try:
            file_path = Path(__file__).parent.parent.parent / \
                "data"/"legends.json"
            with open(file_path, "r", encoding="utf-8") as json_file:
                json_data = json.load(json_file)
                archetype_map = {
                    "Hero": 1,
                    "Mentor": 2,
                    "Shadow": 3,
                    "Trickster": 4,
                    "Shapeshifter": 5,
                    "Threshold Guardian": 6,
                    "Herald": 7,
                    "Ally": 8,
                    "Temptress": 9,
                    "Creator": 10,
                    "Innocent": 11,
                    "Innocent / Warrior": 12,
                    "Destroyer": 13
                }
        except (FileNotFoundError, json.JSONDecodeError, PermissionError) as e:
            raise Exception(f"Failed to load JSON file {e}")
        try:
            for item in json_data:
                archetype_name = item["archetype"]
                if archetype_name:
                    archetype_number = archetype_map[archetype_name]
                else:
                    archetype_number = 14 
                CharacterCard.objects.get_or_create(
                    id=item['id'],
                    name=item['name'],
                    archetype_id=archetype_number
                )
        except (ValueError, IntegrityError) as e:
            raise Exception(f"Failed to create character card {e}")
