import sys

from PEPPSaF.Application.Console.ConsoleApplication import Application as ConsoleApplication
from PEPPSaF.Application.Tools.ToolApplication import Application as ToolApplication

if __name__ == "__main__":
    Application = ToolApplication(sys.argv) if len(sys.argv) > 1 else ConsoleApplication(sys.argv)
    exit("Exited with code: " + str(Application.run()))
