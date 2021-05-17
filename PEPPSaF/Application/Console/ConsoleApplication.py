from time import sleep

from PEPPSaF.Application.Application import Application as BaseApplication
from PEPPSaF.Application.Models.Sensors.GarageLightMqtt import GarageLightMqtt
from PEPPSaF.Application.Models.Sensors.YellowLightSensor import YellowLightSensor
from PEPPSaF.Concerns.OpcuaSensor import OpcuaSensor
from PEPPSaF.Concerns.mqtt_sensor import mqtt_sensor


class Application(BaseApplication):
    sensors_mqtt: list = [
        GarageLightMqtt
    ]
    sensors_opcua: list = [
        YellowLightSensor
    ]

    def run(self) -> int:
        if self.get_arg(1) == "MQTT":
            return self.mqtt_run()
        return self.opcua_run()

    @staticmethod
    def check_sensor_mqtt(sensor: mqtt_sensor):
        print("Checking " + sensor.get_name() + ": Pending")
        sensor.subscribe()
        print(" -- Sensor " + str(sensor.get_name()) + " in " + str(sensor.get_topic()) + " is " + str(
            sensor.get_value()))
        print("Checking " + sensor.get_name() + ": Done")

    def mqtt_run(self):
        while True:
            choice = input("If you want to quit type Quit: ")
            if choice == "Quit":
                return 0
            for sensor in self.sensors_mqtt:
                self.check_sensor_mqtt(sensor())
            sleep(self.config().get_attribute('sleep', 0.002))

    def opcua_run(self):
        while True:
            choice = input("If you want to quit type Quit: ")
            if choice == "Quit":
                return 0
            for sensor in self.sensors_opcua:
                self.check_sensor_opcua(sensor())
            sleep(self.config().get_attribute('sleep', 0.002))

    @staticmethod
    def check_sensor_opcua(sensor: OpcuaSensor):
        print("Checking " + sensor.name + ": Pending")
        print(" -- Sensor ns=" + str(sensor.namespace_index) + ";i=" + str(sensor.identifier) + " is " + str(
            sensor.value()))
        print("Checking " + sensor.name + ": Done")
