from psa.accao import Mover
from psa.util import mover
from psa.util import dist

class OperadorMover():

    @property
    def accao(self):
        return self.accao

    def OperadorMover(self, modelo_mundo, ang):
        self.__modelo_mundo = modelo_mundo
        self.__ang = ang
        self.accao = Mover(ang, ang_abs = True)

    def aplicar(self, estado):
        novo_estado = mover(estado, self.__ang)
        elem = self.__modelo_mundo.get_elem(novo_estado)
        if elem is not 'obs':
            return novo_estado
        else:
            return None

    def custo(self, estado, novo_estado):
        return max(dist(estado, novo_estado), 1)