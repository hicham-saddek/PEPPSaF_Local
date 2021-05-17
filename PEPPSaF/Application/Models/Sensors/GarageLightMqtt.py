from PEPPSaF.Concerns.mqtt_sensor import mqtt_sensor


class GarageLightMqtt(mqtt_sensor):
    name: str = "GarageLight-01"
    topic: str = "house/garage/light/bulb-01"
