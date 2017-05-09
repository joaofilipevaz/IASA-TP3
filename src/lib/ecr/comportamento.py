import abc


class Comportamento:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def activar(self, percepcao):
        """Activa resposta"""
