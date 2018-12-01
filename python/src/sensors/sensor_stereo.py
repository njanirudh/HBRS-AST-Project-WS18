from sensors import sensor_abstract_class

class SensorStereo(sensor_abstract_class.SensorAbstractClass):

    def __init__(self):
        super().__init__()

        self.name = "Stereo Camera"
        self.sensor_data = [('knife',1, 55), ('scissor', 2, 95), ('fork', 3, 99),
                            ('spoon', 4, 99), ('keys', 5, 95)]

    def run_sensor(self):
        pass

    def get_results(self):
        return self.sensor_data

    def __str__(self):
        return self.name

if __name__ == '__main__':
    ss = SensorStereo()
