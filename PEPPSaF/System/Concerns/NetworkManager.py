import socket

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
            if "host" not in interface or "port" not in interface:
                exit("Interfaces should have a host and port value assigned")
            self.send_to(str(interface["host"]), int(interface["port"]), data)

    def send_to(self, host: str, port: int, data: Data):
        sock = socket.socket()
        data.mark_as_sent()
        try:
            sock.connect((host, port))
            byt = data.to_json().encode(self.encoding)
            sock.send(byt)
        except BaseException:
            exit(
                "Something went wrong! cannot reach " + host + ":" + str(port) + " we tried to send: " + data.to_json())
        finally:
            sock.close()
