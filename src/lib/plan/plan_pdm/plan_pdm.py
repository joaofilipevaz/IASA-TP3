from lib.plan.planeador import Planeador
from lib.pdm.pdm import Pdm
from modelo_pdm_plan import ModeloPDMPlan


class PlanPDM(Planeador):

    def __init__(self):
        self.__gama = 0.0
        self.__delta_max = 0
        self.__utilidade = {}
        self.__politica = {}
        self.__pdm = Pdm(self.__gama, self.__delta_max)

    def planear(self, modelo_plan, estado, objectivos):
        if objectivos:
            modelo_pdm_plan = ModeloPDMPlan(modelo_plan, objectivos)
            self.__utilidade, self.__politica = self.__pdm.resolver(modelo_pdm_plan)
        else:
            self.terminar_plano()

    def obter_accao(self, s):
        if self.__politica:
            return self.__politica.get(s)

    def plano_pendente(self):
        return self.__politica

    def terminar_plano(self):
        self.__politica = {}
        self.__utilidade = {}

    def mostrar(self, vis):
        if self.__politica:
            vis.limpar()
            vis.campo(self.__utilidade)
            vis.campo(self.__politica)
