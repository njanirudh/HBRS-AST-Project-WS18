from abc import ABC , abstractmethod

"""
"""
class SensorAbstractClass(ABC):

    def __init__(self):
        """

        """
        super().__init__()
        self.sensor_name = str
        self.sensor_data = []

    @abstractmethod
    def run_sensor(self):
        """

        :return:
        """
        pass

    @abstractmethod
    def get_results(self):
        """

        :return:
        """
        pass

    @abstractmethod
    def __str__(self):
        """

        :return:
        """
        pass
