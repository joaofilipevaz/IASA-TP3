from agente_prosp.controlo import Controlo
from agente_prosp.controlo_aprend.mec_aprend import MecAprend
from psa.util import dirmov

class ControloAprendRef(Controlo):

    def __init__(self):
        self.__rmax = 100
        self.__s = None
        self.__a = dirmov()
        self.__mec_aprend = MecAprend(self.__a)

    def processar(self, percepcao):
        pass

    def __gerar_reforco(self, percepcao):
        r = -percepcao.custo_mov
        if percepcao.carga:
            r += self.__rmax
        elif percepcao.colisao:
            r += -self.__rmax
        return r
