import pprint
from sensor_fusion import SensorFusion

if __name__ == "__main__":

    sensor_fusion = SensorFusion()

    sensor_fusion.add_sensor(None)
    sensor_fusion.add_sensor(None)

    sensor_fusion.process_input()

    sensor_fusion.get_output()