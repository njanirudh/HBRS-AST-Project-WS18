from sensors import sensor_abstract_class

class SensorStereo(sensor_abstract_class.SensorAbstractClass):

    def __init__(self):
        super().__init__()

        self.name = "Stereo Camera"
        self.sensor_data = [('knife',1, 99), ('scissor', 2, 65), ('fork', 3, 33), ('spoon', 4, 80), ('keys', 5, 95)]

    def run_sensor(self):
        pass

    def get_results(self):
        return self.sensor_data

    def __str__(self):
        return self.name

if __name__ == '__main__':
    ss = SensorStereo()
