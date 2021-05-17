import socket

from PEPPSaF.System.Concerns.Data import Data
from PEPPSaF.System.ConfigManager import ConfigManager


class NetworkManager:
    interfaces: dict = {"eth0": "wired.central-node.peppsaf", "wlan0": "wireless.central-node.peppsaf"}
    config_manager: ConfigManager
    encoding: str = "utf-8"

    def __init(self):
        self.config_manager = ConfigManager()
        self.interfaces = self.config_manager.get_attribute('interfaces', self.interfaces)

    def send(self, data: Data):
        for interface in self.interfaces:
            self.send_to(str(interface["host"]), int(interface["port"]), data)

    def send_to(self, host: str, port: int, data: Data):
        sock = socket.socket()
        sock.connect((host, port))
        data.mark_as_sent()
        byt = data.to_json().encode(self.encoding)
        sock.send(byt)
        sock.close()
