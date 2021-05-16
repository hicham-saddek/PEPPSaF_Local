from PEPPSaF.Application.Application import Application as BaseApplication


class Application(BaseApplication):
    def run(self) -> int:
        print(self.get_args())
        return 0
