import socket
import netifaces


class IPDetector:
    @staticmethod
    def detect_by_interface(interface):
        return netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']

    @staticmethod
    def detect_by_host(host):
        return socket.gethostbyname(host)

    @staticmethod
    def available_interfaces():
        return netifaces.interfaces()
