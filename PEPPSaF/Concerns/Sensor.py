class Sensor:
    name: str

    def __init__(self, name: str):
        self.name = name if name is not None else self.name if self.name is not None else self.guess_name()

    def guess_name(self):
        return self.name if self.name is not None else str(type(self).__name__)[:-len('Sensor')]

    def get_name(self):
        return self.name

    def get_value(self) -> str:
        return "None"
