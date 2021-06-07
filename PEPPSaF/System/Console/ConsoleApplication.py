from PEPPSaF.System.Application import Application as BaseApplication
from PEPPSaF.System.Concerns.Data import Data
from PEPPSaF.System.Concerns.DataCollection import DataCollection


class Application(BaseApplication):
    protocol: str = "opcua"
    sensors: list = []

    def run(self):
        while True:
            for sensor in self.sensors:
                self.net_manager.send(Data(sensor()))
            self.sleep()
