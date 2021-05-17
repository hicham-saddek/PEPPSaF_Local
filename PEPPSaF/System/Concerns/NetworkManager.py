import requests

from PEPPSaF.System.Concerns.Data import Data
from PEPPSaF.System.ConfigManager import ConfigManager


class NetworkManager:
    interfaces: dict = None
    config_manager: ConfigManager
    encoding: str = "utf-8"

    def __init__(self):
        self.config_manager = ConfigManager()
        self.interfaces = self.config_manager.get_attribute('interfaces')

    def send(self, data: Data):
        if self.interfaces is None:
            exit("Missing interfaces configurations")
        for interface in self.interfaces:
            interface = self.interfaces[interface]
            if "host" not in interface or "port" not in interface or "uri" not in interface:
                exit("Interfaces should have a host and port and uri value assigned")
            try:
                request = self.send_to(str(interface["host"]), int(interface["port"]), str(interface["uri"]), data)
                if request.status_code < 200 or request.status_code > 400:
                    print("Failed to send Data: ", data.to_json() + " with code: " + str(request.status_code))
                else:
                    print("Received from server(" + interface["host"] + ":" + str(
                        interface["port"]) + ") received: " + str(
                        request.json()))
            except requests.exceptions.ConnectionError as ce:
                print("Connection error, trying again...")

    @staticmethod
    def send_to(host: str, port: int, uri: str, data: Data):
        request = requests.post(host + ":" + str(port) + "/" + uri, {"data": data.mark_as_sent().to_json()})
        return request
