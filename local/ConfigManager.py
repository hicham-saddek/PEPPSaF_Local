import json


class ConfigManager:
    path = "config.peppsaf"
    configurations = {}

    def __init__(self):
        with open(self.path) as file:
            data = json.load(file)
        self.set(data)

    def set(self, configurations):
        self.configurations = configurations
        return self

    def get_attribute(self, attribute: str):
        return self.configurations[attribute]

    def set_attribute(self, attribute: str, value):
        self.configurations[attribute] = value
        return self

    def save(self):
        with open(self.path, 'w') as file:
            json.dump(self.configurations, file)
