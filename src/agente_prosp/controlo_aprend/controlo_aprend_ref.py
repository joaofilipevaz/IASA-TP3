from agente_prosp.controlo import Controlo
from agente_prosp.controlo_aprend.mec_aprend import MecAprend
from psa.util import dirmov
#from psa.psa5.actuador import Mover
from psa.accao import Mover
import psa.util


class ControloAprendRef(Controlo):

    def __init__(self):
        self.__rmax = 100
        self.__s = None
        self.__a = dirmov()
        self.__mec_aprend = MecAprend(self.__a)

    def processar(self, percepcao):
        sn = percepcao.posicao
        if self.__s is not None:
            a = percepcao.orientacao
            r = self.__gerar_reforco(percepcao)
            self.__mec_aprend.aprender(self.__s, a, r, sn)

        an = self.__mec_aprend.seleccionar_accao(sn)
        self.__s = sn
        if an is not None:
            #self.mostrar(self.__s)
            return Mover(an, ang_abs=True)

    def __gerar_reforco(self, percepcao):
        r = -percepcao.custo_mov
        if percepcao.carga:
            r += self.__rmax
        elif percepcao.colisao:
            r += -self.__rmax
        return r

    def mostrar(self, s):
        vis = psa.vis(1)
        vis.limpar()
        self.__mec_aprend.mostrar(s, vis)