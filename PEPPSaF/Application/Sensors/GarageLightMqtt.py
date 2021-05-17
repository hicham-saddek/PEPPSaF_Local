from PEPPSaF.Concerns.mqttsensor import MqttSensor


class GarageLightMqtt(MqttSensor):
    name: str = "GarageLight-01"
    topic: str = "house/garage/light/bulb-01"
