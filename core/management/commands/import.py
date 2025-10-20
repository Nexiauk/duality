"""
Custom management command to import character data
from a json file
"""
from django.core.management.base import BaseCommand
from django.db import IntegrityError
from core.models import CharacterCard
import json


class Command(BaseCommand):
    help = "Imports character objects from legends.json file"

    def handle(self):
        """
        Imports character data from a raw json file into the 
        CharacterCard model.
        Reads the JSON file with multiple character objects, each with a unique ID
        and creates corresponding records in the CharacterCard table.

        Fields in the json file that don't exist in the Django model are ignored.
        The JSON id field is mapped directly to the CharacterCard
        Primary Key.

        An error is raised if the file isn't found.
        """
        try:
            with open("legends.json") as json_file:
                json_data = json.load(json_file)
        except (FileNotFoundError, json.JSONDecodeError, PermissionError) as e:
                raise Exception(f"Failed to load JSON file {e}")
        try:
                for item in json_data:
                    CharacterCard.objects.get_or_create(
                        id = item['id'],
                        name = item['name'],
                    )
        except (ValueError, IntegrityError) as e:
             raise Exception(f"Failed to create character card {e}")
            
