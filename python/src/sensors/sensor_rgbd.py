from sensors import sensor_abstract_class

"""
"""
class SensorRGBD(sensor_abstract_class.SensorAbstractClass):

    def __init__(self):
        super().__init__()
        self.name = "RGDB Sensor"
        self.sensor_data = [("knife",1, 99), ("scissor", 2, 65),
                            ("spoon", 3, 33), ("spoon", 4, 80), ("keys", 5, 95)]

    def run_sensor(self):
        pass

    def get_results(self):
        return self.sensor_data

    def __str__(self):
        return self.name

if __name__ == "__main__":
    sr = SensorRGBD()
