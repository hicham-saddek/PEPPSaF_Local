from PEPPSaF.System.Application import Application as BaseApplication
from PEPPSaF.Concerns.IPDetector import IPDetector


class Application(BaseApplication):
    def run(self) -> int:
        while True:
            menu = "////////////////////// - MENU - //////////////////////////\n"
            menu += "| 1- Find host using network interface name.             |\n"
            menu += "| 2- Find host using host name.                          |\n"
            menu += "| 3- Show all interfaces with appropriate IP addresses.  |\n"
            menu += "| 4- Show all interfaces with appropriate IP/Hostname.   |\n"
            menu += "//////////////////////////////////////////////////////////\n"
            print(menu)
            menu = input("Choice (type quit to end): ")
            if str(menu) == "quit":
                print("Bye bye !")
                return 0
            menu = int(menu)
            if menu == 1:
                while True:
                    print("Available interfaces are: " + str(IPDetector.available_interfaces()))
                    interface = input("Select a network interface (Type quit to go back to the main menu): ")
                    if interface == "quit":
                        break
                    print(str(IPDetector.detect_by_interface(interface)))
            if menu == 2:
                while True:
                    hostname = input("Select a hostname (Type quit to go back to the main menu): ")
                    if hostname == "quit":
                        break
                    print(IPDetector.detect_by_host(hostname))
            if menu == 3:
                print(str(IPDetector.get_interfaces_with_ip(True)))
            if menu == 4:
                print(str(IPDetector.get_interfaces_with_host_and_ip(True)))
            self.clear_screen()
