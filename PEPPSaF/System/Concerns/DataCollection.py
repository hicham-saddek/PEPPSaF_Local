import json

from PEPPSaF.System.Concerns.Data import Data


class DataCollection:
    collection = []

    def __init__(self):
        self.collection = []

    def items(self):
        return self.collection

    def add(self, data: Data) -> list:
        self.collection.append(data.to_obj())
        return self.collection

    def count(self) -> int:
        return len(self.collection)

    def to_json(self) -> str:
        return json.dumps(self.collection)

    def empty(self):
        self.collection = []
        return self

    def remove(self, data: Data):
        self.collection.remove(data)
        return self

    def __str__(self) -> str:
        return self.to_json()
