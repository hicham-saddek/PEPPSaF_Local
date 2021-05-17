from PEPPSaF.Concerns.Data import Data
from PEPPSaF.Concerns.DataCollection import DataCollection
from PEPPSaF.System.Application import Application as BaseApplication


class Application(BaseApplication):
    protocol: str = "opcua"
    sensors_mqtt: list = []
    sensors_opcua: list = []

    def run(self) -> int:
        collection = DataCollection()
        for sensor in self.sensors_opcua if self.protocol == "opcua" else self.sensors_mqtt if self.protocol == "mqtt" else []:
            collection.add(Data(sensor()))
        if collection.count() >= 1:
            self.send_data_to_central(collection)
        return 0

    def send_data_to_central(self, collection: DataCollection):
        data = collection.to_json()
        print(data)
