from psa.psa5.util import dirmov
from agente_prosp.controlo_delib.operador_mover import OperadorMover


class ModeloMundo:

    def __init__(self):
        self.__estado = None
        self.__estados = []
        self.__operadores = [OperadorMover(self, ang) for ang in dirmov]
        self.__alterado = False
        #definicao do nada
        self.__elementos = {}

    @property
    def estado(self):
        return self.__estado

    @property
    def alterado(self):
        return self.__alterado

    def obter_elem(self, estado):
        return self.__elementos[estado]

    def actualizar(self, percepcao):
        # posicao agente
        self.__estado = percepcao.actualizar
        if self.__elementos.gravados != self.__elementos.percepcao:
            self.__estados = self.__estados.percepcao
            self.__elementos = self.__elementos.percepcao
            self.__alterado = True
        else:
            self.__alterado = False

    def operadores(self):
        return self.operadores()

    def estados(self):
        return self.__estados

    def mostrar(self, vis):
        lista_obs = ["alvo", "obstaculo"]
        alvos_obs = {key: value for (key, value) in self.__elementos.items() if value in lista_obs}
        vis.elementos(alvos_obs)
