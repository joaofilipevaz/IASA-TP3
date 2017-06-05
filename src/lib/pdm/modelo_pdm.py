import abc


class ModeloPDM:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def S(self):
        """lista de estados"""

    @abc.abstractmethod
    def A(self, estado):
        """lista de operadores"""

    @abc.abstractmethod
    def T(self, s, a):
        """lista de transicoes"""

    @abc.abstractmethod
    def R(self, s, a, sn):
        """resposta"""
