import sys

from PEPPSaF.Application.Console import Application as Console
from PEPPSaF.System.Tools.ToolApplication import Application as Tools

if __name__ == "__main__":
    if 1 in sys.argv and sys.argv[1] == "tools":
        print("|- --- --- --- -| P E P P S a F |- --- --- --- -|")
        Application = Tools(sys.argv)
        exit("Exited with code: " + str(Application.run()))
    elif 1 in sys.argv and  sys.argv[1] == "console":
        print("|- --- --- --- -| P E P P S a F |- --- --- --- -|")
        Application = Console(sys.argv)
        exit("Exited with code: " + str(Application.run()))
    exit("Missing running method, please type 'console.py tools' or 'console.py console' to start the PEPPSaF local")
