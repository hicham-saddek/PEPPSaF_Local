import json
import os.path


class ConfigManager:
    path = "config.peppsaf"
    configurations = {}

    def __init__(self):
        self.path = os.path.realpath(self.path)
        with open(self.path) as file:
            data = json.load(file)
        self.set(data)

    def set(self, configurations):
        self.configurations = configurations
        return self

    def get_attribute(self, attribute: str, default=None):
        if attribute not in self.configurations:
            return default
        return self.configurations[attribute]

    def set_attribute(self, attribute: str, value):
        self.configurations[attribute] = value
        return self

    def save(self):
        with open(self.path, 'w') as file:
            json.dump(self.configurations, file, sort_keys=True)
