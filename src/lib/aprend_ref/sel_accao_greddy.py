from lib.aprend_ref.memoria_aprend import MemoriaAprend
from lib.aprend_ref.sel_accao import SelAccao


class SelAccaoEGreedy(MemoriaAprend, SelAccao):

    def __init__(self, mem_aprend, accoes, epsilon):
        self.__epsilon = epsilon
        self.__mem_aprend = mem_aprend

    def seleccionar_accao(self, s):
        pass

    def max_accao(self, s):
        pass

    def explorar(self, s):
        pass
