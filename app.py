import sys

from PEPPSaF.Application.Console import Application as Console
from PEPPSaF.System.Tools.ToolApplication import Application as Tools

if __name__ == "__main__":
    if len(sys.argv) > 1 and str(sys.argv[1]) == "tools":
        print("|- --- --- --- -| P E P P S a F |- --- --- --- -|")
        Application = Tools(sys.argv)
        exit("Exited with code: " + str(Application.run()))
    elif len(sys.argv) > 1 and str(sys.argv[1]) == "console":
        print("|- --- --- --- -| P E P P S a F |- --- --- --- -|")
        Application = Console(sys.argv)
        exit("Exited with code: " + str(Application.run()))
    exit("Missing running method, please type 'app.py tools' or 'app.py console' to start the PEPPSaF local")
