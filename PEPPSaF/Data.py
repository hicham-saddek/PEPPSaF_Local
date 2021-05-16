import json


class Data:
    sensor = ""
    value = False
    timestamp = 0

    def __init__(self, sensor: str, value: int, timestamp: int):
        self.set_sensor(sensor).set_value(value).set_timestamp(timestamp)

    def set_sensor(self, sensor: str):
        self.sensor = sensor
        return self

    def set_value(self, value: int):
        self.value = value
        return self

    def set_timestamp(self, timestamp: int):
        self.timestamp = timestamp
        return self

    def get_sensor(self):
        return self.sensor

    def get_value(self):
        return self.value

    def get_timestamp(self):
        return self.timestamp

    def to_object(self):
        return {"sensor": self.get_sensor(), "value": self.get_value(), "timestamp": self.get_timestamp()}

    def to_json(self):
        return json.encoder.JSONEncoder.encode(self.to_object())
