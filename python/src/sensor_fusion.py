from enum import Enum
from sensors import sensor_abstract_class


class SensorFusion:
    """

    """

    def __init__(self):
        """

        """
        self.sensors_list = []
        self.fusion_list = []

    def add_sensor(self,in_sensor):
        """

        :param in_sensor:
        :return:
        """
        #if not isinstance(in_sensor,int):
        self.sensors_list.append(in_sensor)

    def __sort_fusion_list(self, in_fusion_list):
        """

        :param in_sensor_list:
        :return:
        """
        def takeSecond(elem):
            return elem[1]

        in_fusion_list.sort(key=takeSecond)
        print(in_fusion_list)


    def process_input(self):
        """

        :param in_algorithm_type:
        :return:
        """
        for sensor in self.sensors_list:
            self.fusion_list.append(sensor.sensor_data)

        self.__sort_fusion_list(self.fusion_list)


    def get_output(self):
        """

        :return:
        """
        pass




