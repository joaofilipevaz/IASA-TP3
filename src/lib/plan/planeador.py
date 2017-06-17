import abc


class Planeador:
    _metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def planear(self, modelo_plan, estado_inicial, objectivos):
        "abstract"

    @abc.abstractmethod
    def obter_accao(self, estado):
        "abstract"

    @abc.abstractmethod
    def plano_pendente(self):
        "abstract"

    @abc.abstractmethod
    def terminar_plano(self):
        "abstract"

    @abc.abstractmethod
    def mostrar(self, vis, s):
       "abstract"
