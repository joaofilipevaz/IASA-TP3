from lib.plan.planeador import Planeador

class PlanPEE(Planeador):

    def __init__(self, mec_pee):
        self.__plano = []
        self.__mec_pee = mec_pee


    def planear(self, modelo_plan, estado_inicial, objectivos):
        self.__plano = objectivos


    def obter_Accao(self, estado):
        return self.__plano.pop(0)


    def plano_pendente(self):
        if len(self.__plano) > 0:
            return True
        return False


    def terminar_plano(self):
        self.__plano = []