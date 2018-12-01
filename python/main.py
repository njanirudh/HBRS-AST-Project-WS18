import pprint
from sensor_fusion import SensorFusion
from sensors import sensor_rgbd
from sensors import sensor_stereo
if __name__ == "__main__":

    sensor_fusion = SensorFusion()

    s1 = sensor_rgbd.SensorRGBD()
    sensor_fusion.add_sensor(s1)

    s2 = sensor_stereo.SensorStereo()
    sensor_fusion.add_sensor(s2)

    sensor_fusion.process_input()

    sensor_fusion.get_output()
