from PEPPSaF.System.Console.ConsoleApplication import Application as BaseApplication
from PEPPSaF.Application.Sensors.WachT7waMzyanSensor import WachT7waMzyanSensor


class Application(BaseApplication):
    protocol = "opcua"
    sensors = [WachT7waMzyanSensor]
