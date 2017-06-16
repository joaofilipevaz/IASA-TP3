from lib.aprend_ref.memoria_aprend import MemoriaAprend
from lib.aprend_ref.sel_accao import SelAccao
from random import random, choice, shuffle


class SelAccaoEGreedy(MemoriaAprend, SelAccao):

    def __init__(self, mem_aprend, accoes, epsilon):
        self.__epsilon = epsilon
        self.__mem_aprend = mem_aprend
        self.__accoes = accoes

    def seleccionar_accao(self, s):
        if random() > self.__epsilon:
            accao = self.max_accao(s)
        else:
            accao = self.explorar(s)
        return accao

    def max_accao(self, s):
        accoes = shuffle(self.__accoes)
        return max(accoes, key=lambda a: self.__mem_aprend.obter(s, a))

    def explorar(self, s):
        return choice(self.__accoes)
