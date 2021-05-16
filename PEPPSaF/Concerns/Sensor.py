import json

from PEPPSaF.Concerns.SAFDeckManager import SAFDeckManager


class Sensor:
    name: str = None
    topic: str = None
    deck: SAFDeckManager = None
    value: str = None
    charset: str = "utf-8"

    def guess_name(self) -> str:
        return self.name if self.name is not None else str(type(self).__name__).strip('Sensor')

    def set_name(self, name: str):
        self.name = name
        return self

    def __init__(self, topic: str = None, name: str = None):
        self.set_topic(topic if topic is not None else self.get_topic())
        self.set_name(name if name is not None else self.get_name())
        self.set_deck(SAFDeckManager())
        self.set_on_message()
        self.get_deck().connect()
        self.get_deck().get_client().loop_start()

    def set_on_message(self):
        def on_message(client, userdata, message):
            data = str(message.payload.decode(self.charset))
            if message.topic == self.get_topic():
                self.set_value(data)

        self.get_deck().get_client().on_message = on_message

    def set_deck(self, deck: SAFDeckManager):
        self.deck = deck
        return self

    def get_deck(self) -> SAFDeckManager:
        return self.deck

    def get_name(self) -> str:
        return self.guess_name()

    def set_topic(self, topic: str):
        self.topic = topic
        return self

    def get_topic(self):
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

    def __delete__(self, instance):
        self.disconnect()
