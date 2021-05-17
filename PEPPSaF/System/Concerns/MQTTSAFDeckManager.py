import json

from paho.mqtt.client import Client as MQTTClient, Client

from PEPPSaF.System.ConfigManager import ConfigManager


class MQTTSAFDeckManager:
    host: str = "test.mosquitto.org"
    port: int = 1883
    keepalive: int = 60
    client: MQTTClient = None
    clean_session: bool = True
    client_id: str = None
    transport: str = "tcp"

    def __init__(self):
        config = ConfigManager().get_attribute('mqtt_clients')
        if config is None:
            exit("Configuration missing: mqtt_clients")
        if "port" in config:
            self.set_port(config["port"] if config["port"] is not None else self.get_port())
        if "host" in config:
            self.set_host(config["host"] if config["host"] is not None else self.get_host())
        if "keepalive" in config:
            self.set_keepalive(config["keepalive"] if config["keepalive"] is not None else self.get_keepalive())
        if "clean_session" in config:
            self.set_clean_session(
                config["clean_session"] if config["clean_session"] is not None else self.get_clean_session())
        if "transport" in config:
            self.set_transport(config["transport"] if config["transport"] is not None else self.get_transport())
        self.set_client(self.new_client())

    def new_client(self) -> Client:
        def on_connect(client, userdata, flags, rc):
            client.connected_flag = rc == 0
            # print("Connected OK" if rc == 0 else str("Bas connection returned code=" + str(rc)))

        client = Client(
            client_id=self.get_client_id(),
            clean_session=self.get_clean_session(),
            userdata=None,
            transport=self.get_transport()
        )
        client.on_connect = on_connect

        return client

    def set_transport(self, transport: str = "tcp"):
        self.transport = transport
        return self

    def get_transport(self):
        return self.transport

    def set_client_id(self, client_id: str):
        self.client_id = client_id
        return self

    def get_client_id(self):
        return self.client_id

    def set_clean_session(self, clean: bool):
        self.clean_session = clean
        return self

    def get_clean_session(self):
        return self.clean_session

    def set_port(self, port: int):
        self.port = port
        return self

    def set_host(self, host: str):
        self.host = host
        return self

    def set_keepalive(self, keepalive: int):
        self.keepalive = keepalive
        return self

    def get_port(self):
        return self.port

    def get_host(self):
        return self.host

    def get_keepalive(self):
        return self.keepalive

    def set_client(self, client: MQTTClient):
        self.client = client
        return self

    def get_client(self):
        return self.client

    def to_obj(self):
        return self.__dict__

    def to_json(self):
        return json.dumps(self.to_obj())

    def connect(self):
        try:
            self.get_client().connect(
                host=self.get_host(),
                port=self.get_port(),
                keepalive=self.get_keepalive()
            )
        except ConnectionRefusedError:
            exit("Too many attempts to the broker, please change the configurations")

    def __str__(self):
        return self.to_json()

    def disconnect(self):
        self.get_client().disconnect()
