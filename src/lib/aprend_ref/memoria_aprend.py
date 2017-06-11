import abc


class MemoriaAprend:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def actualizar(self, s, a, q):
        """void"""

    @abc.abstractmethod
    def obter(self, s, a):
        """double"""
