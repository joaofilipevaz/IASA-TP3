import abc

class ModeloPlan:
    _metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def estados(self):
        """processa"""

    @abc.abstractmethod
    def operadores(self):
        """processa"""
