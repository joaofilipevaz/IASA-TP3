from lib.aprend_ref.memoria_aprend import MemoriaAprend
from lib.aprend_ref.aprend_ref import AprendRef
from lib.aprend_ref.memoria_esparsa import MemoriaEsparsa
from lib.aprend_ref.sel_accao import SelAccao
from lib.aprend_ref.aprend_q import AprendQ
from lib.aprend_ref.sel_accao_greddy import SelAccaoEGreedy
import psa.psa5 as psa


class MecAprend(SelAccao):

    def __init__(self, accoes, alfa=1, gama=0.9, epsilon=0.1, nsim=100):
        self.__accoes = accoes
        self.__mem_aprend = MemoriaEsparsa()
        self.__sel_accao = SelAccaoEGreedy(self.__mem_aprend, self.__accoes, epsilon)
        self.__aprend_ref = AprendQ(self.__mem_aprend, self.__sel_accao, alfa, gama)

    def aprender(self, s, a, r, sn):
        self.__aprend_ref.aprender(s, a, r, sn)

    def seleccionar_accao(self, s):
        return self.__sel_accao.seleccionar_accao(s)

    def mostrar(self, s, vis):
        #vis.limpar()
        vis.aprendref(self.__aprend_ref)
        vis.accoesestado(s, self.__accoes, self.__mem_aprend.get_memoria)
