from time import sleep

from PEPPSaF.System.Concerns.Data import Data
from PEPPSaF.System.Concerns.DataCollection import DataCollection
from PEPPSaF.System.Application import Application as BaseApplication


class Application(BaseApplication):
    protocol: str = "opcua"
    sensors: list = []

    def run(self):
        while True:
            collection = DataCollection().empty()
            for sensor in self.sensors:
                collection.add(Data(sensor()))
            if collection.count() >= 1:
                self.send_data_to_central(collection)
            sleep(self.config().get_attribute('sleep', 0.002))

    @staticmethod
    def send_data_to_central(collection: DataCollection):
        data = collection.to_json()
        print(data)
