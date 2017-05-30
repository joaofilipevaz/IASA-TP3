import abc


class Controlo(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def processar(self, percepcao):
        """accao"""
