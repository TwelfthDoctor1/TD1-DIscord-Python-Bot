import os
import urllib.request
import urllib.error
from pathlib import Path
from UtilLib.JSONParser import json_load
from UtilLib.LoggerService import BaseLoggerService


class JSONHandlerService(BaseLoggerService):
    pass


JSON_LIB = os.path.join(Path(__file__).resolve().parent.parent, "JSONLib")
BASE_URL = "https://raw.githubusercontent.com/TwelfthDoctor1/TD1-Discord-Python-Bot/main/JSONLib/"

JSONHANDLER_SERVICE = JSONHandlerService()


class JSONHandler:
    """
    JSONHandler

    A class that is able to acquire JSON data from GitHub or from JSONLib.
    """
    def __init__(self, json_data_name: str, json_use_git: bool = True):
        """
        Initialise JSONHandler to acquire data.
        :param json_data_name: Name of JSON File, with .json suffix
        :param json_use_git: Whether JSON Data should be acquired Online or Offline
        """
        self.json = json_data_name
        self.json_data = None or dict
        self.git_use = json_use_git

        # Formulate JSON -> Acquire Data from Provided Values
        self.formulate_json()

    def formulate_json(self):
        def offline_formulation():
            json_dir = os.path.join(JSON_LIB, self.json + ".json")

            with open(json_dir, "r") as json_ref:
                self.json_data = json_load(json_ref.read())
                json_ref.close()

            return True

        def online_formulation():
            json_url = BASE_URL + self.json + ".json"
            json_req = urllib.request.Request(url=json_url, method="GET")

            try:
                with urllib.request.urlopen(json_req) as response:
                    self.json_data = json_load(response.read().decode("utf-8"))

                    return True

            except urllib.error.URLError as e:
                JSONHANDLER_SERVICE.error(
                    f"[FAILURE IN GETTING VERSION IN GITHUB] Either the associated URL is invalid or that the data is not raw "
                    f"or may be caused by other issues."
                    f"\nPerhaps Check your internet connection?"
                )

                if hasattr(e, "code") and hasattr(e, "reason"):
                    # HTTP Error Code + Reason
                    JSONHANDLER_SERVICE.error(f"HTTP ERROR CODE {e.code} | {e.reason}")

                elif hasattr(e, "reason"):
                    # HTTP Error Reason
                    JSONHANDLER_SERVICE.error(f"FAILURE REASON | {e.reason}")

                else:
                    # Exception Error Dump
                    JSONHANDLER_SERVICE.error(f"RAW FAILURE REASON | {e}")

                return False

        if self.git_use is False:
            offline_formulation()

        can_acquire = online_formulation()

        if can_acquire is False:
            offline_formulation()

    def return_json(self):
        return self.json_data

    def return_specific_json(self, key):
        return self.json_data[key]
