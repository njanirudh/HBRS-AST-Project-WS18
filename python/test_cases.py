import unittest

from sensor_fusion import SensorFusion
from sensors import sensor_rgbd
from sensors import sensor_stereo


class TestingList(unittest.TestCase):
    def initializing_lists(self):
        """
        Initializing the output list of the program and expected list of the user
        :return:
        """
        sensor_fusion = SensorFusion()

        s1 = sensor_rgbd.SensorRGBD()
        sensor_fusion.add_sensor(s1)

        s2 = sensor_stereo.SensorStereo()
        sensor_fusion.add_sensor(s2)

        sensor_fusion.process_input()

        self.output_list = sensor_fusion.get_output()
        self.expected_list = [('knife', 1, 99), ('scissor', 2, 95), ('fork', 3, 99), ('spoon', 4, 99), ('keys', 5, 95)]

        return self.output_list, self.expected_list

    def test_list_count(self):
        """
        Checks if the output and expected output list have the
        same length
        :return: Bool
        """
        output, expected = TestingList.initializing_lists(self)
        self.assertCountEqual(output, expected)

    def test_list_elem(self):
        """
        Checks if the output and expected output list are the same
        :return: Bool
        """
        output, expected = TestingList.initializing_lists(self)
        self.assertListEqual(output, expected)


if __name__ == "__main__":
    unittest.main()