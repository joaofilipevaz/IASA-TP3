from lib.pdm.modelo_pdm import ModeloPDM

class Pdm(ModeloPDM):

    def __init__(self, gama, delta_max):
        self.__gama = gama
        self.__delta_max = delta_max



    def utilidade(self, modelo):
        S = modelo.S
        A = modelo.A
        R = modelo.R
        T = modelo.T
        gama = self.__gama
        U = { s:0 for s in S()}
        while True:
            Uant = U.copy()
            delta = 0
            for s in S():
                U[s] = max(self.util_accao(s, a, Uant, modelo)) for a in A(s)
                delta = max(delta, abs(U[s] - Uant[s]))
            # se o delta for menor que o delta max
            if delta < self.__delta_max:
                break


    def util_Accao(self, s, a, U, modelo):

                U[s] = max(p*R(s, a, sn) + gama*Uant[sn]) for ()

