import os
from pathlib import Path
from UtilLib.JSONParser import json_load

JSON_LIB = os.path.join(Path(__file__).resolve().parent.parent, "JSONLib")


class JSONHandler:
    def __init__(self, json_data_name: str):
        self.json = json_data_name
        self.json_data = None or dict

        self.formulate_json()

    def formulate_json(self):
        json_dir = os.path.join(JSON_LIB, self.json + ".json")

        with open(json_dir, "r") as json_ref:
            self.json_data = json_load(json_ref.read())
            json_ref.close()

    def return_json(self):
        return self.json_data

    def return_specific_json(self, key):
        return self.json_data[key]
