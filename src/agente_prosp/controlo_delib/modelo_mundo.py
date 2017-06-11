from psa.util import dirmov
from lib.plan.modelo_plan import ModeloPlan


class ModeloMundo(ModeloPlan):

    def __init__(self):
        self.estado = None
        self.__estados = []
        self.__operadores = [OperadorMover(self, ang) for ang in dirmov]
        self.alterado = False
        #definicao do nada
        self.__elementos = {}

    @property
    def estado(self):
        return self.estado

    @property
    def alterado(self):
        return self.alterado

    @property
    def __elementos(self, map<K, V>):

    def obter_elem(self, estado):
        return self.elementos[estado]

    def actualizar(self, percepcao):
        self.estado = percepcao.actualizar #posição agente
        if self.elementos.gravados != self.elementos.percepcao:
            self.estados = self.__estados.percepcao
            self.elementos = self.elementos.percepcao
            self.alterado = True
        else:
            self.alterado = False

    def operadores(self):
        return self.operadores()

    def estados(self):
        return self.__estados

