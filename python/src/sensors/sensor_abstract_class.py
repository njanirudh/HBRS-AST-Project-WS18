from abc import ABC, abstractmethod
from enum import Enum

"""
Abstract class which all sensor classes should inherit.
"""

class ALGO(Enum):
    ImageMatching = 1
    SemanticSegmentation = 2

class SensorAbstractClass(ABC):

    def __init__(self):
        """
        Initializing the basic data of the class
        and sensor
        """
        super().__init__()
        self.sensor_name = str
        self.sensor_data = []
        self.algo = ALGO.ImageMatching

    @abstractmethod
    def set_algorithm(self,in_algo):
        """
        Setting the algorithm to be used on the
        data of the sensor
        :return: None
        """
        pass

    @abstractmethod
    def run_sensor(self):
        """
        Method to extract data from the sensor ,
        preprocess the result run any algorithm
        on the sensor data.
        :return: None
        """
        pass

    @abstractmethod
    def get_results(self):
        """
        Returns the processed data of the sensor.
        :return: list of results
        """
        pass

    @abstractmethod
    def __str__(self):
        """
        Return the details like name , sensor ID etc
        :return: string
        """
        pass
