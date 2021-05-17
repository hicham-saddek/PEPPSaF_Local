import sys

from PEPPSaF.Application.Console.ConsoleApplication import Application as ConsoleApplication
from PEPPSaF.Application.Tools.ToolApplication import Application as ToolApplication

if __name__ == "__main__":
    Application = ToolApplication(sys.argv) if len(sys.argv) > 2 else ConsoleApplication(sys.argv)
    print("|- --- --- --- -| P E P P S a F |- --- --- --- -|")
    exit("Exited with code: " + str(Application.run()))
