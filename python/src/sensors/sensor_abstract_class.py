from abc import ABC , abstractmethod

class SensorAbstractClass(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def set_parameters(self):
        pass

    @abstractmethod
    def run_sensor(self):
        pass

    @abstractmethod
    def get_results(self):
        pass

    @abstractmethod
    def __str__(self):
        pass
