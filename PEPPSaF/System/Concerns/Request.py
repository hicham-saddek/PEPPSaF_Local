import requests

class Request:
    protocol: str = "http"
    host: str = "localhost"
    port: int = 80
    uri: str = ""
    response: requests = None
    data: dict = {}
    debug: bool = False
    show_errors: bool = True

    def __init__(self, interface: dict = {}, data: dict = {}, debug: bool = False, show_errors: bool = False):
        self.set_from_interface(interface)
        self.set_data(data)
        self.debug = debug
        self.show_errors = show_errors

    def get_url(self) -> str:
        return "{}://{}:{}/{}".format(self.protocol, self.host, self.port, self.uri)


    def set_host(self, host: str = "LOCALHOST"):
        self.host = host
        return self

    def set_protocol(self, protocol: str = "HTTP"):
        self.protocol = protocol
        return self

    def set_port(self, port: int = 80):
        self.port = port
        return self

    def set_uri(self, uri: str = ""):
        self.uri = uri
        return self

    def set_data(self, data):
        self.data = data
        return self

    def get_data(self):
        return self.data

    def post(self) -> bool:
        try:
            self.log_sending()
            self.response = requests.post(self.get_url(), {"data": self.get_data()})
        except requests.exceptions.ConnectionError as exception:
            self.log_error()
        if self.good(): self.log_success() 
        else: self.log_error()
        return self.good()

    def status_code(self)->int:
        return self.response.status_code
            

    def good(self) -> bool:
        if self.response == None: return False
        return not self.bad()

    def bad(self) -> bool:
        return self.status_code() < 200 or self.status_code() >= 400

    def set_from_interface(self, interface: dict):
        if "host" not in interface or "port" not in interface or "uri" not in interface or "protocol" not in interface:
            return self
        self.set_host(interface["host"]).set_protocol(interface["protocol"]).set_port(interface["port"]).set_uri(interface["uri"])
        return self
    
    def log_error(self):
        if self.debug or self.show_errors: print("REQUEST MANAGER: Failed to send data({}) to ({}) with status code: {}!".format(str(self.get_data()), str(self.get_url()), self.status_code()))

    def log_success(self):
        if self.debug: print("REQUEST MANAGER: Successfuly sent data({}) to ({}) with status code: {}!".format(str(self.get_data()), str(self.get_url()), self.status_code()))

    def log_sending(self):
        if self.debug: print("REQUEST MANAGER: Sending ({}) via POST to ({})...".format(self.get_data(), self.get_url()))