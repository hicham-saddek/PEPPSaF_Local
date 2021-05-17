from time import sleep

from PEPPSaF.System.Application import Application as BaseApplication
from PEPPSaF.System.Concerns.Data import Data
from PEPPSaF.System.Concerns.DataCollection import DataCollection
from PEPPSaF.System.Concerns.NetworkManager import NetworkManager


class Application(BaseApplication):
    protocol: str = "opcua"
    sensors: list = []

    def run(self):
        while True:
            collection = DataCollection().empty()
            for sensor in self.sensors:
                collection.add(Data(sensor()))
            if collection.count() >= 1:
                for data in collection.items():
                    NetworkManager().send(data)
            self.sleep()
