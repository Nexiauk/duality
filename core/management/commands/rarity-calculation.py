"""
Custom management command to import character data
from a json file
"""
from django.core.management.base import BaseCommandcalc
from pathlib import Path
import json


class Command(BaseCommand):
    """
    Custom Django management command to load character data from a JSON file,
    calculate the total power for each character by summing their powerstats,
    and print a sorted list of all total power values.

    Reads 'legends.json' from the 'data' directory relative to this
    command file.
    Handles file not found, JSON decode, and permission errors
    Outputs a list of total power values sorted from lowest to highest.

    This command is intended for inspection and analysis of the power range,
    not for modifying the database.
    """
    def handle(self, *args, **kwargs):
        try:
            file_path = Path(__file__).parent.parent.parent / \
                "data"/"legends.json"
            with open(file_path, "r", encoding="utf-8") as json_file:
                json_data = json.load(json_file)
        except (FileNotFoundError, json.JSONDecodeError, PermissionError) as e:
            raise Exception(f"Failed to load JSON file {e}")
        power_array = []
        for item in json_data:
            total_power = sum(item["powerstats"].values())
            power_array.append(total_power)
        power_array.sort()
        print(power_array)
