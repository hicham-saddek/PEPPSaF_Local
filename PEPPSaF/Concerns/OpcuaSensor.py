from PEPPSaF.Concerns.OPCUASAFDeckManager import OPCUASAFDeckManager


class OpcuaSensor:
    name: str = None
    identifier: int
    namespace_index: int
    deck: OPCUASAFDeckManager = None

    def guess_name(self) -> str:
        return self.name if self.name is not None else str(type(self).__name__)[:-len('Sensor')]

    def __init__(self, name: str = None, identifier: int = None, namespace_index: int = None):
        self.namespace_index = namespace_index if namespace_index is not None else self.namespace_index
        self.name = name if name is not None else self.name if self.name is not None else self.guess_name()
        self.identifier = identifier if identifier is not None else self.identifier
        self.deck = OPCUASAFDeckManager()

    def value(self):
        return self.deck.get_node(identifier=self.identifier, namespace_index=self.namespace_index).get_value()
