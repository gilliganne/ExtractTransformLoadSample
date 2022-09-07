# TODO: set up class to configure database (input will be data from local_config.json)
import os
from pathlib import Path
import json

config_file_path = Path(__file__).resolve().parent


class ConfigBase(object):
    def __init__(self):
        self.config_dict = {}
        self._set_config_dict()
        self.db_dict = self.config_dict["database"]
    #     TODO: missing attributes  fill here

    def _set_config_dict(self):
        with open(f"{config_file_path}/local_config.json", "r") as f:
            self.config_dict = json.loads(f.read())