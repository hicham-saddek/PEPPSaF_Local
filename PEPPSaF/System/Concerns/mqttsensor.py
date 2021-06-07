import json

from PEPPSaF.System.Concerns.MQTTSAFDeckManager import MQTTSAFDeckManager
from PEPPSaF.System.Concerns.Sensor import Sensor


class MqttSensor(Sensor):
    topic: str = None
    deck: MQTTSAFDeckManager = None
    value: str = None
    charset: str = "utf-8"

    def set_name(self, name: str):
        self.name = name
        return self

    def __init__(self, topic: str = None, name: str = None):
        super().__init__(name)
        self.set_topic(topic if topic is not None else self.get_topic())
        self.set_deck(MQTTSAFDeckManager())
        self.set_on_message()
        self.connect()
        self.get_deck().get_client().loop_start()

    def connect(self):
        super(MqttSensor, self).connect()
        self.get_deck().connect()

    def set_on_message(self):
        def on_message(client, userdata, message):
            data = str(message.payload.decode(self.charset))
            if message.topic == self.get_topic():
                self.set_value(data)

        self.get_deck().get_client().on_message = on_message

    def set_deck(self, deck: MQTTSAFDeckManager):
        self.deck = deck
        return self

    def get_deck(self) -> MQTTSAFDeckManager:
        return self.deck

    def set_topic(self, topic: str):
        self.topic = topic
        return self

    def get_topic(self) -> str:
        return self.topic

    def subscribe(self):
        self.get_deck().get_client().subscribe(self.get_topic())

    def publish(self, value: str):
        print("Publishing: (" + value + ") to topic: " + self.get_topic())
        self.get_deck().get_client().publish(self.get_topic(), value)

    def set_value(self, value: str):
        self.value = value
        return self

    def get_value(self) -> str:
        return self.value

    def __str__(self) -> str:
        return json.dumps({
            "name": self.get_name(),
            "topic": self.get_topic(),
            "value": self.get_value()
        })

    def disconnect(self):
        self.get_deck().get_client().loop_stop()
