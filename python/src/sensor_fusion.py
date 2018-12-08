class SensorFusion:
    """
    Converting the list of input data to single list of objects with the
    highest confidence
    """

    def __init__(self):
        """
        Initializing the input and output lists
        """
        self.sensors_list = []
        self.fusion_list = []
        self.output_list = []

    def add_sensor(self, in_sensor):
        """
        Creates a single list of all the sensors
        :param in_sensor: input sensor
        :return: None
        """
        self.sensors_list.append(in_sensor)

    def __sort_fusion_list(self, in_fusion_list):
        """
        Sorts the single list of all the data of various sensors
        :param in_sensor_list: input sensor list
        :return: None
        """

        def __sort_by_id(in_element):
            return in_element[1]

        in_fusion_list.sort(key=__sort_by_id)

    def __get_maximum_confidence(self, in_sorted_list):
        """
        Results in the list of maximum confidence of objects from the input data
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

        :param in_algorithm_type:
        :return:
        """
        for sensor in self.sensors_list:
            self.fusion_list.extend(sensor.sensor_data)

        self.__sort_fusion_list(self.fusion_list)
        self.__get_maximum_confidence(self.fusion_list)

    def get_output(self):
        """
        Returns the output list
        :return:
        """
        return self.output_list
