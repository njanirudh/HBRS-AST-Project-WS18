from pprint import pprint

from sensor_fusion import SensorFusion
from sensors import sensor_rgbd
from sensors import sensor_stereo

if __name__ == "__main__":

    # Creating the sensor fusion object
    sensor_fusion = SensorFusion()

    # Adding sensors to the sensor fusion
    s1 = sensor_rgbd.SensorRGBD()
    sensor_fusion.add_sensor(s1)

    s2 = sensor_stereo.SensorStereo()
    sensor_fusion.add_sensor(s2)

    # Process the results from all the sensors
    sensor_fusion.process_input()

    # Returs the output of the sensor fusion object
    pprint(sensor_fusion.get_output())
