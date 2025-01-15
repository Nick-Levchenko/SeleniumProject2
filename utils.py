import json


class ConfigReader:
    CONFIG_FILE = "config.json"

    def read_config(self, config_name):
        with open(self.CONFIG_FILE, 'r') as json_file:
            config = json.load(json_file)
            return config[config_name]


class ListUtils:

    @staticmethod
    def sorting_by_descending(some_list):
        return some_list == sorted(some_list, reverse=True)


