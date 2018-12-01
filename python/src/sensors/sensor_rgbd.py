from sensors import sensor_abstract_class

class SensorRGBD(sensor_abstract_class.SensorAbstractClass):

    def __init__(self):
        super().__init__()

    def run_sensor(self):
        pass

    def get_results(self):
        pass

    def __str__(self):
        pass

if __name__ == "__main__":
    sr = SensorRGBD()
