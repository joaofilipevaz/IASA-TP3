from psa.psa5.accao import Mover
from psa.psa5.util import mover
from psa.psa5.util import dist
from pee.modprob.operador import Operador

class OperadorMover(Operador):

    @property
    def accao(self):
        return self.__accao

    def __init__(self, modelo_mundo, ang):
        self.__modelo_mundo = modelo_mundo
        self.__ang = ang
        self.__accao = Mover(ang, ang_abs=True)

    def aplicar(self, estado):
        novo_estado = mover(estado, self.__ang)
        elem = self.__modelo_mundo.obter_elem(novo_estado)
        if elem in ["vazio", "alvo"]:
            return novo_estado

    def custo(self, estado, novo_estado):
        return max(dist(estado, novo_estado), 1)
