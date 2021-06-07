from PEPPSaF.System.Concerns.Request import Request
from PEPPSaF.System.Concerns.Data import Data
from PEPPSaF.System.ConfigManager import ConfigManager


class NetworkManager:
    interfaces: dict = None
    config_manager: ConfigManager
    encoding: str = "utf-8"

    def __init__(self):
        self.interfaces = ConfigManager().get_attribute('interfaces')

    def send(self, data: Data):
        if self.interfaces is None: exit("Missing interfaces configurations")
        for interface in self.interfaces:
            request = Request(
                self.interfaces[interface], 
                data.sent_over(self.interfaces[interface]).mark_as_sent().to_json(), show_errors=True
            ).post()