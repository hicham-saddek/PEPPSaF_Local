class Sensor:
    name: str
    connected: bool = False

    def __init__(self, name: str):
        self.name = name if name is not None else self.name if self.name is not None else self.guess_name()

    def guess_name(self) -> str:
        return self.name if self.name is not None else self.generate_name()

    def generate_name(self) -> str:
        return str(type(self).__name__)[:-len("Sensor")] if str(type(self).__name__).find("Sensor") != -1 else str(type(self).__name__)


    def get_name(self):
        return self.name

    def get_value(self) -> str:
        return "None"

    def disconnect(self):
        pass

    def __del__(self):
        try:
            if self.connected:
                self.disconnect()
        except OSError:
            pass

    def connect(self):
        self.connected = True
        pass
