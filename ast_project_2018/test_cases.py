import sys
import unittest

sys.path.append('./src')

from sensor_fusion import SensorFusion
from sensors import sensor_rgbd
from sensors import sensor_stereo


class TestingList(unittest.TestCase):
    def initializing_lists(self):
        """
        Initializing
        the output list of the program and expected list of the user
        :return:
        """
        sensor_fusion = SensorFusion()

        s1 = sensor_rgbd.SensorRGBD()
        s1.sensor_data = [("knife", 1, 99), ("fork", 3, 99)]
        s1.set_algorithm(s1.algo.SemanticSegmentation)
        sensor_fusion.add_sensor(s1)

        s2 = sensor_stereo.SensorStereo()
        s2.sensor_data = [("knife", 1, 94), ("knife", 1, 69), ("knife", 1, 89)]
        s2.set_algorithm(s1.algo.SemanticSegmentation)
        sensor_fusion.add_sensor(s2)

        sensor_fusion.process_input()

        self.output_list = sensor_fusion.get_output()
        print("???", self.output_list)

        self.expected_list = [("knife", 1, 99), ("fork", 3, 99)]
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
