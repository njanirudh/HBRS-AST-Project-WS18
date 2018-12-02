from abc import ABC, abstractmethod

"""
Abstract class which all algorithm classes should inherit.
"""
class AlgorithmAbstractClass(ABC):


    def __init__(self):
        """
        Initialize the internal data structures
        related to the algorithm.
        """
        super().__init__()

    @abstractmethod
    def set_input(self):
        """
        Set the input data that the algorithm
        class will store
        :return: None
        """
        pass

    @abstractmethod
    def process_input(self):
        """
        The function where the actual processing
        of the data takes place
        :return: None
        """
        pass

    @abstractmethod
    def get_output(self):
        """
        Returns the processed result of the algorithm
        as a JSON object
        :return: Json string
        """
        pass
