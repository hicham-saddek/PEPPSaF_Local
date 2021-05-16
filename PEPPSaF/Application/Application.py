import os

from PEPPSaF.Application.ConfigManager import ConfigManager


class Application:
    arguments = ()
    clear_screen_commands = {"windows": "cls", "linux": "clear"}
    config_manager = None

    def set_args(self, arguments):
        self.arguments = arguments
        return self

    def get_args(self):
        return self.arguments

    def get_arg(self, argument):
        if argument in self.get_args():
            return self.get_args()[argument]
        return None

    def __init__(self, arguments=()):
        self.config_manager = ConfigManager()
        self.set_args(arguments)

    def run(self) -> int:
        print(str(self.get_args()))
        return 0

    def clear_screen(self):
        os.system(self.clear_screen_commands["windows"] if os.name == 'nt' else self.clear_screen_commands["linux"])

    def config(self) -> ConfigManager:
        return self.config_manager
