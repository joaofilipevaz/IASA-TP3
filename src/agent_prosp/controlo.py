import abc


class Controlo:
    _metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def processar(self, processar):
        """processa"""
