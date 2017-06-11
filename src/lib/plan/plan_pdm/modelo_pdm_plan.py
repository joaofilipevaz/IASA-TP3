

class ModeloPDMPlan():

    #def __init__(self):

    def __iniciar_modelo(self, modelo_plan):
        self.__S=modelo_plan.estados()
        self.__A=modelo_plan.operadores()
        for s in self.__S:
            for a in self.__A:
                self.__gerar_modelo(s,a)

    def __gerar_modelo(self, s, a):
        sn = a.aplicar(s)
        if sn is None:
            self.__T[(s,a)]=[]
        else:
            self.__T[(s,a)]=[(1,sn)]
            self.__R[(s,a,sn)]= self.__gerar_recompensa(s,a,sn)

    def __gerar_recompensa(self, s, a, sn):
        r = -a.custo(s,sn)
        if sn in self.__objectivos:
            r += self.rmax
        return r

    def estados(self):
        return self.__S

    def operadores(self):
        return self.__A

    def S(self):
        return self.__S

    def A(self, estado):
        return self.__A(estado)

    def T(self, s, a):
        return self.__T[(s, a)]

    def R(self, s, a, sn):
        return self.__R[(s, a, sn)]
