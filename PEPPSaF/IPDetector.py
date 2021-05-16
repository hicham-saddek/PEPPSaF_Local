import socket

import netifaces


class IPDetector:
    @staticmethod
    def get_interface(interface: str):
        return netifaces.ifaddresses(interface)

    @staticmethod
    def detect_by_interface(interface: str):
        interface = IPDetector.get_interface(interface)
        if 2 in interface:
            return str(interface[netifaces.AF_INET][0]['addr'])
        return "No IPv4 Address in this interface"

    @staticmethod
    def detect_by_host(host: str):
        return socket.gethostbyname(host)

    @staticmethod
    def available_interfaces():
        return netifaces.interfaces()

    @staticmethod
    def get_interfaces_with_ip(show_only_available: bool):
        interfaces_ip = {}
        interfaces = IPDetector.available_interfaces()
        for interface in interfaces:
            ip = IPDetector.detect_by_interface(interface)
            if show_only_available:
                if ip != "No IPv4 Address in this interface":
                    interfaces_ip[interface] = {"IP": ip}
                continue
            interfaces_ip[interface] = {"IP": IPDetector.detect_by_interface(interface)}
        return interfaces_ip

    @staticmethod
    def get_interfaces_with_host_and_ip(show_only_available: bool):
        interfaces_ip = {}
        interfaces = IPDetector.available_interfaces()
        for interface in interfaces:
            ip = IPDetector.detect_by_interface(interface)
            if show_only_available:
                if ip != "No IPv4 Address in this interface":
                    interfaces_ip[interface] = {"IP": ip, "Hostname": socket.gethostbyaddr(ip)[0]}
                continue
            interfaces_ip[interface] = {"IP": IPDetector.detect_by_interface(interface)}
        return interfaces_ip
