from django.apps import AppConfig
import json
from pathlib import Path


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        file_path = Path(__file__).parent/"data"/"legends.json"
        with open(file_path, "r", encoding="utf-8") as json_file:
            json_data = json.load(json_file)
            from .data import datastore
            datastore.legends = json_data
