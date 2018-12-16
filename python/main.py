from pprint import pprint
import os, sys

sys.path.append('./src')

from sensor_fusion import SensorFusion
from sensors import sensor_rgbd
from sensors import sensor_stereo

if __name__ == "__main__":

    # Creating the sensor fusion object
    sensor_fusion = SensorFusion()

    # Adding sensors to the sensor fusion
    s1 = sensor_rgbd.SensorRGBD()
    s1.sensor_data = [("knife", 1, 99), ("fork", 3, 99)]
    s1.set_algorithm(s1.algo.ImageMatching)
    sensor_fusion.add_sensor(s1)

    s2 = sensor_rgbd.SensorRGBD()
    s2.sensor_data = [("knife", 1, 94), ("knife", 1, 69), ("knife", 1, 89)]
    s2.set_algorithm(s2.algo.SemanticSegmentation)
    sensor_fusion.add_sensor(s2)

    # s3 = sensor_stereo.SensorStereo()
    # s3.set_algorithm(s3.algo.ImageMatching)
    # sensor_fusion.add_sensor(s3)
    #
    # s4 = sensor_stereo.SensorStereo()
    # s4.set_algorithm(s4.algo.SemanticSegmentation)
    # sensor_fusion.add_sensor(s4)

    # Process the results from all the sensors
    sensor_fusion.process_input()

    # Returs the output of the sensor fusion object
    pprint(sensor_fusion.get_output())
