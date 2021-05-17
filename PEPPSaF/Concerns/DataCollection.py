import json

from PEPPSaF.Concerns.Data import Data


class DataCollection:
    collection = []

    def add(self, data: Data) -> list:
        self.collection.append(data)
        return self.collection

    def count(self) -> int:
        return len(self.collection)

    def to_json(self) -> str:
        collection = []
        for data in self.collection:
            collection.append(data.to_obj())
        return json.dumps(collection)

    def __str__(self) -> str:
        return self.to_json()
