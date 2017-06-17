from lib.pdm.modelo_pdm import ModeloPDM
from lib.plan.modelo_plan import ModeloPlan


class ModeloPDMPlan(ModeloPDM, ModeloPlan):

    def __init__(self, modelo_plan, objectivos):
        self.__S = []
        self.__A = []
        self.__T = {}
        self.__R = {}
        self.__rmax = 20
        self.__objectivos = objectivos
        self.__iniciar_modelo(modelo_plan)

    def __iniciar_modelo(self, modelo_plan):
        self.__S = modelo_plan.estados()
        self.__A = modelo_plan.operadores()
        print self.__A
        print modelo_plan.operadores()
        for s in self.__S:
            for a in self.__A:
                self.__gerar_modelo(s, a)

    def __gerar_modelo(self, s, a):
        sn = a.aplicar(s)
        if sn is not None:
            self.__T[(s, a)] = [(1, sn)]
            self.__R[(s, a, sn)] = self.__gerar_recompensa(s, a, sn)
        else:
            self.__T[(s, a)] = []

    def __gerar_recompensa(self, s, a, sn):
        r = -a.custo(s, sn)
        if sn in self.__objectivos:
            r += self.__rmax
        return r

    def S(self):
        return self.__S

    def A(self, s):
        return self.__A

    def T(self, s, a):
        return self.__T[(s, a)]

    def R(self, s, a, sn):
        return self.__R[(s, a, sn)]
