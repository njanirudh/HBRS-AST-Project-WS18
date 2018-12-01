from abc import ABC , abstractmethod

class AlgorithmAbstractClass(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def set_input(self):
        pass

    @abstractmethod
    def set_json_parameters(self):
        pass

    @abstractmethod
    def process(self):
        pass

    @abstractmethod
    def get_output(self):
        pass



