"""
Custom management command to import character data
from a json file
"""
from django.core.management.base import BaseCommand
from core.models import CharacterCard
import json


class Command(BaseCommand):
    help = "Imports character objects from legends.json file"

    def handle(self):
        """
        
        """
        with open("legends.json") as json_file:
            json_data = json.load(json_file)
            for item in json_data:
                CharacterCard.objects.get_or_create(
                    id=item['id'],
                    name=item['name'],
                )
