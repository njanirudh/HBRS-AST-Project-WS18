from enum import Enum
from sensors import sensor_abstract_class

class ALGORITHMS(Enum):
    MAX = 1
    AVERAGE = 2


class SensorFusion:

    def __init__(self):
        self.sensors_list = []
        self.fusion_list = []

    def add_sensor(self,in_sensor):
        #if not isinstance(in_sensor,int):
        pass

    def __sort_fusion_list(self):
        pass

    def process_input(self,in_algorithm_type = ALGORITHMS.MAX):

        if in_algorithm_type == 1 :
            pass


    def get_output(self):
        pass




