from lib.pee.modprob.problema_heur import ProblemaHeur
from psa.util import dist

class ProblemaPlan(ProblemaHeur):

    def __init__(self, estado_inicial, estado_final, operadores):
        super(ProblemaPlan, self).__init__(estado_inicial, estado_final, operadores)
        self.__estado_final = estado_final

    def objectivo(self, estado):
        if estado == self.__estado_final:
            return True
        else:
            return False

    def heuristica(self, estado):
        return dist(estado, self.__estado_final)
