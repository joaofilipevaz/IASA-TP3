from agente_prosp.controlo import Controlo
from agente_prosp.controlo_aprend.mec_aprend import MecAprend
from psa.psa5.util import dirmov
from psa.psa5.actuador import Mover

class ControloAprendRef(Controlo):

    def __init__(self):
        self.__rmax = 100
        self.__s = None
        self.__a = dirmov()
        self.__mec_aprend = MecAprend(self.__a)

    def processar(self, percepcao):
        sn = percepcao.posicao
        if self.s is not None:
            a = percepcao.orientacao
            r = self.__gerar_reforco(percepcao)
            self.__mec_aprend.aprender(self.s, a, r, sn)
        an = self.__mec_aprend.seleccionar_accao(sn)
        self.s = sn
        if an is not None:
            return Mover(an, arg_abs=True)

    def __gerar_reforco(self, percepcao):
        r = -percepcao.custo_mov
        if percepcao.carga:
            r += self.__rmax
        elif percepcao.colisao:
            r += -self.__rmax
        return r
