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
        shuffle(self.__accoes)

    def explorar(self, s):
        choice(self.__accoes)
