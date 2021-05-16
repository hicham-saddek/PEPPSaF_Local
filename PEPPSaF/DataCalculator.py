from PEPPSaF.Data import Data


class DataCalculator:
    @staticmethod
    def calculate_timestamp(data1: Data, data2: Data):
        return data1.get_timestamp() - data2.get_timestamp()