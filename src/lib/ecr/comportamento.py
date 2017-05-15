import abc


class Comportamento(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def activar(self, percepcao):
        """Activa resposta"""
