from PEPPSaF.Application.Sensors.RedLightSensor import RedLightSensor
from PEPPSaF.Application.Sensors.YellowLightSensor import YellowLightSensor
from PEPPSaF.System.Console.ConsoleApplication import Application as BaseApplication


class Application(BaseApplication):
    protocol = "opcua"
    sensors = [YellowLightSensor, RedLightSensor]
