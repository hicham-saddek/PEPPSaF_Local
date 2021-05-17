from opcua.ua import UaStatusCodeError
from opcua.ua.uaerrors import BadAttributeIdInvalid

from PEPPSaF.System.Concerns.OPCUASAFDeckManager import OPCUASAFDeckManager
from PEPPSaF.System.Concerns.Sensor import Sensor


class OpcuaSensor(Sensor):
    name: str = None
    identifier: int
    namespace_index: int
    deck: OPCUASAFDeckManager = OPCUASAFDeckManager()

    def __init__(self, name: str = None, identifier: int = None, namespace_index: int = None):
        super().__init__(name)
        self.namespace_index = namespace_index if namespace_index is not None else self.namespace_index
        self.identifier = identifier if identifier is not None else self.identifier
        self.deck = OPCUASAFDeckManager()
        self.connect()

    def get_value(self):
        if self.connected:
            try:
                return self.deck.get_node(identifier=self.identifier, namespace_index=self.namespace_index).get_value()
            except OSError:
                return "os error"
            except BadAttributeIdInvalid:
                return "Bad attribute id - invalid"

    def disconnect(self):
        self.deck.disconnect()

    def connect(self):
        try:
            super(OpcuaSensor, self).connect()
            self.deck.connect()
        except UaStatusCodeError:
            exit("Cannot connect")
