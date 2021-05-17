import json
import time

from PEPPSaF.System.Concerns.Sensor import Sensor


class Data:
    sensor: Sensor
    arrived_at: time = time.time()
    sent_at: time

    def __init__(self, sensor: Sensor):
        self.sensor = sensor
        self.sent_at = 0

    def mark_as_sent(self):
        self.sent_at = time.time()

    def to_obj(self) -> dict:
        return {
            "sensor": self.sensor.get_name(),
            "value": self.sensor.get_value(),
            "arrived_at": int(self.arrived_at),
            "sent_at": int(self.sent_at)
        }

    def to_json(self):
        return json.dumps(self.to_obj())

    def __str__(self):
        return self.to_json()
