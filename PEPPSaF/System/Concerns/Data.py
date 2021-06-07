import json
from datetime import datetime

from PEPPSaF.System.Concerns.OpcuaSensor import OpcuaSensor
from PEPPSaF.System.Concerns.Sensor import Sensor
from PEPPSaF.System.ConfigManager import ConfigManager


class Data:
    sensor: OpcuaSensor
    arrived_at: datetime = None
    sent_at: datetime = None
    hostname: str = ""
    over: str = ""

    def __init__(self, sensor: Sensor):
        self.sensor = sensor
        self.mark_as_arrived()
        self.hostname = ConfigManager().get_attribute("hostname", self.hostname)

    def mark_as_sent(self):
        self.sent_at = datetime.utcnow()
        return self

    def mark_as_arrived(self):
        self.arrived_at = datetime.utcnow()
        return self

    def sent_over(self, interface: dict):
        self.over = interface['host']
        return self

    def to_obj(self):
        return {
            "name": self.sensor.get_name(),
            "identifier": self.sensor.identifier,
            "namespace": self.sensor.namespace_index,
            "value": self.sensor.get_value(),
            "hostname": self.hostname,
            "arrived_at": str(self.arrived_at.isoformat(timespec='microseconds'))+"Z",
            "sent_at": str(self.sent_at.isoformat(timespec='microseconds'))+"Z" if self.sent_at is not None else str(""),
            "received_at": str(""),
            "over": self.over
        }

    def __dict__(self):
        return self.to_obj()

    def to_json(self):
        return json.dumps(self.to_obj())

    def __str__(self):
        return self.to_json()
