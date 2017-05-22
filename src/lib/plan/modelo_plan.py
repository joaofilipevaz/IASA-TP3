import abc

class ModeloPlan:
    _metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def estados(self, processar):
        """processa"""

    @abc.abstractmethod
    def operadores(self, processar):
        """processa"""
