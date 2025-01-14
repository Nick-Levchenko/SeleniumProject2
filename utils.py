import json


class ConfigReader:
    CONFIG_FILE = r"C:\Users\leva0\PycharmProjects\SeleniumProject2\config.json"

    def timeout(self):
        with open(self.CONFIG_FILE, 'r') as json_file:
            config = json.load(json_file)
            return config['timeout']


# сделал класс как-бы на "будущее", если понадобятся еще какие-то сортировки
class ListSorter:

    @staticmethod
    def sorting_by_descending(some_list):
        return some_list == sorted(some_list, reverse=True)
