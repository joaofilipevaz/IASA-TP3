import abc


class SelAccao:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def seleccionar_accao(self, s):
        """accao"""
