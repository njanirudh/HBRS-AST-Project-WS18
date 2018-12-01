from sensor_fusion import SensorFusion
from sensors import sensor_rgbd
from sensors import sensor_stereo


def test_1():
    """
    Checks if the input data type is correct or not
    :return: Bool
    """
    in_value_1 = []
    in_value_2 = str


def test_2():
    """
    Checks if the output values are correct for given sensor input values.
    :return: Bool
    """
    sensor_fusion = SensorFusion()

    s1 = sensor_rgbd.SensorRGBD()
    sensor_fusion.add_sensor(s1)

    s2 = sensor_stereo.SensorStereo()
    sensor_fusion.add_sensor(s2)

    sensor_fusion.process_input()

    print(sensor_fusion.get_output())


if __name__ == "__main__":
    test_1()
    test_2()
