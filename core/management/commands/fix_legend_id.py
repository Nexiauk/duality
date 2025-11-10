"""
Management command to transform character data.
"""
import json
from django.core.management.base import BaseCommand
from pathlib import Path


class Command(BaseCommand):
    """
    Reads exported CharacterCard model data from a json file
    then gives each item a new field called 'legend_id' that matches
    the original 'pk'.
    Data is exported into a new file.
    """
    def handle(self, *args, **kwargs):
        file_path = Path(__file__).parent.parent.parent / \
            "data"/"charactercard.json"
        with open(file_path, "r", encoding="utf-8") as json_file:
            json_data = json.load(json_file)
            for item in json_data:
                if "pk" in item:
                    item["fields"]["legend_id"] = item["pk"]
        second_file_path = Path(__file__).parent.parent.parent / \
            "data"/"charactercard_with_legend_id2.json"
        with open(second_file_path, "w", encoding="utf-8") as json_file:
            json.dump(json_data, json_file)
