from random import random, choice
import numpy as np


class SelAccaoEGreedy:

    def __init__(self, mem_aprend, accoes, epsilon):
        self.__epsilon = epsilon
        self.__mem_aprend = mem_aprend
        self.__accoes = accoes

    def seleccionar_accao(self, s):
        if random() > self.__epsilon:
            accao = self.max_accao(s)
            print "esmifra"
        else:
            accao = self.explorar(s)
            print "explorar"
        return accao

    def max_accao(self, s):
        np.random.shuffle(self.__accoes)
        return max(self.__accoes, key=lambda a: self.__mem_aprend.obter(s, a))

    def explorar(self, s):
        return choice(self.__accoes)
