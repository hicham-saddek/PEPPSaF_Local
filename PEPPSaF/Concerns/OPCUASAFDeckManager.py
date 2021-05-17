import json

from opcua import Client

from PEPPSaF.System.ConfigManager import ConfigManager


class OPCUASAFDeckManager:
    config_manager: ConfigManager
    configurations: dict
    host: str = "opc.tcp://localhost"
    port: int = 4840
    uri: str = "OPCUA/SimulationServer"
    url: str = None
    client: Client = None
    timeout: int = 4

    def to_json(self):
        return json.dumps(self.__dict__)

    def __str__(self):
        return self.to_json()

    def __init__(self):
        self.config_manager = ConfigManager()
        self.configurations = self.config_manager.get_attribute('opcua-clients')
        if self.configurations is None:
            exit("Missing OPCUA Clients configurations")
        if "host" in self.configurations:
            self.host = self.configurations["host"] if self.configurations["host"] is not None else self.host
        if "port" in self.configurations:
            self.port = self.configurations["port"] if self.configurations["port"] is not None else self.port
        if "uri" in self.configurations:
            self.uri = self.configurations["uri"] if self.configurations["uri"] is not None else self.uri
        if "timeout" in self.configurations:
            self.timeout = self.configurations["timeout"] if self.configurations[
                                                                 "timeout"] is not None else self.timeout
        self.build_url()
        self.build_client()
        self.connect()

    def build_url(self) -> str:
        self.url = self.host + ":" + str(self.port) + "/" + self.uri
        return self.url

    def build_client(self) -> Client:
        self.client = Client(url=self.url, timeout=self.timeout)
        return self.client

    def connect(self):
        return self.client.connect()

    def disconnect(self):
        return self.client.disconnect()

    def root(self):
        return self.client.get_root_node()

    def get(self, path: list):
        return self.root().get_child(path)

    def get_node(self, identifier: int, namespace_index: int):
        return self.client.get_node("ns=" + str(namespace_index) + ";i=" + str(identifier))

    def get_children(self):
        return self.root().get_children()

    def __delete__(self, instance):
        self.disconnect()
