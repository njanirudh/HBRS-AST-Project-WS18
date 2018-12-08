import pprint

"""
Class for processing the outputs af all the sensors and processing
them to give final output
"""
class SensorFusion:


    def __init__(self):
        """
        Initializing the input and output list data
        of the class
        """
        self.sensors_list = []
        self.fusion_list = []
        self.output_list = []

    def add_sensor(self, in_sensor):
        """
        Adding sensors to the sensor function object
        :param in_sensor: sensor object
        :return: None
        """
        self.sensors_list.append(in_sensor)

    def __sort_fusion_list(self, in_fusion_list):
        """
        Sorts the list of all the sensor data associated
        with sensor fusion object.
        :param in_sensor_list: input sensor list
        :return: None
        """
        def __sort_by_id(in_element):
            return in_element[1]

        in_fusion_list.sort(key=__sort_by_id)

    def __get_maximum_confidence(self, in_sorted_list):
        """
        Generate the list of maximum confidence of objects
        from the processed input sensor data
        :return: None
        """

        def __sort_by_confidence(in_element):
            return in_element[2]

        try:
            max_id = in_sorted_list[-1][1]

            for index in range(1, max_id + 1):
                current_index = []

                for item in in_sorted_list:
                    if index == item[1]:
                        current_index.append(item)
                max_tuple = max(current_index, key=__sort_by_confidence)
                self.output_list.append(max_tuple)

        except:
            print("Error : Empty list ")

    def process_input(self):
        """
        The functions called to process the added sensor
        data.
        :return: None
        """

        for sensor in self.sensors_list:
            self.fusion_list.extend(sensor.sensor_data)

        self.__sort_fusion_list(self.fusion_list)
        self.__get_maximum_confidence(self.fusion_list)

    def get_output(self):
        """
        Returns the output list of the processed sensor data
        :return: list of output
        """

        return self.output_list
