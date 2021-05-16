from PEPPSaF.IPDetector import IPDetector

if __name__ == "__main__":
    while True:
        menu = "////////////////////// - MENU - //////////////////////////\n"
        menu += "| 1- Find host using network interface name.             |\n"
        menu += "| 2- Find host using host name.                          |\n"
        menu += "//////////////////////////////////////////////////////////\n"
        print(menu)
        menu = input("Choice (type quit to end): ")
        if str(menu) == "quit":
            exit()
        if int(menu) == 1:
            while True:
                print("Available interfaces are: ")
                for i in IPDetector.available_interfaces():
                    print(i)
                interface = input("Select a network interface (Type quit to go back to the main menu): ")
                if interface == "quit":
                    break
                print(IPDetector.detect_by_interface(interface))
        if int(menu) == 2:
            while True:
                hostname = input("Select a hostname (Type quit to go back to the main menu): ")
                if hostname == "quit":
                    break
                print(IPDetector.detect_by_host(hostname))
