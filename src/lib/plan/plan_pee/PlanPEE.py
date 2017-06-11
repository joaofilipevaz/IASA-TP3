from lib.plan.planeador import Planeador
from lib.plan.plan_pee.ProblemaPlan import ProblemaPlan


class PlanPEE(Planeador):

    def __init__(self, mec_pee):
        self.__plano = None
        self.__mec_pee = mec_pee

    def planear(self, modelo_plan, estado_inicial, objectivos):
        problema = ProblemaPlan(estado_inicial, objectivos[0], modelo_plan.objectivos())
        solucao = self.__mec_pee.resolver(problema)
        if solucao:
            self.__plano = [no.operador for no in solucao[1:]]

    def obter_accao(self, estado):
        if self.__plano:
            return self.__plano.pop(0)

    def plano_pendente(self):
        return self.__plano

    def terminar_plano(self):
        self.__plano = None
