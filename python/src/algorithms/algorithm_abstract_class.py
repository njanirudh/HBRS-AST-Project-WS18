from abc import ABC , abstractmethod

"""
"""
class AlgorithmAbstractClass(ABC):
    """

    """
    def __init__(self):
        """

        """
        super().__init__()

    @abstractmethod
    def set_input(self):
        """

        :return:
        """
        pass

    @abstractmethod
    def process_input(self):
        """

        :return:
        """
        pass

    @abstractmethod
    def get_output(self):
        """

        :return:
        """
        pass



