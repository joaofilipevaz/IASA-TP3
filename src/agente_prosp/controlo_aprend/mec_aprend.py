from lib.aprend_ref.memoria_aprend import MemoriaAprend
from lib.aprend_ref.aprend_ref import AprendRef
from lib.aprend_ref.sel_accao import SelAccao


class MecAprend(SelAccao):

    def __init__(self, accoes):
        self.__accoes = accoes
        self.__mem_aprend = MemoriaAprend()
        self.__sel_accao = SelAccao()
        self.__aprend_ref = AprendRef(self.__mem_aprend, self.__sel_accao)

    def aprender(self, s, a, r, sn):
        pass

    def seleccionar_accao(self, s):
        pass
