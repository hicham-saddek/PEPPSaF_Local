from opcua.ua.uaerrors import BadAttributeIdInvalid

from PEPPSaF.Concerns.OPCUASAFDeckManager import OPCUASAFDeckManager
from PEPPSaF.Concerns.Sensor import Sensor


class OpcuaSensor(Sensor):
    name: str = None
    identifier: int
    namespace_index: int
    deck: OPCUASAFDeckManager = None

    def __init__(self, name: str = None, identifier: int = None, namespace_index: int = None):
        super().__init__(name)
        self.namespace_index = namespace_index if namespace_index is not None else self.namespace_index
        self.identifier = identifier if identifier is not None else self.identifier
        self.deck = OPCUASAFDeckManager()

    def get_value(self):
        try:
            return self.deck.get_node(identifier=self.identifier, namespace_index=self.namespace_index).get_value()
        except BadAttributeIdInvalid:
            return "Invalid"
