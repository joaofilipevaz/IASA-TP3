class Pdm:

    def __init__(self, gama, delta_max):
        self.__gama = gama
        self.__delta_max = delta_max

    def utilidade(self, modelo):
        S = modelo.S
        A = modelo.A
        U = {s: 0 for s in S()}
        while True:
            Uant = U.copy()
            delta = 0
            for s in S():
                U[s] = max(self.util_accao(s, a, Uant, modelo) for a in A(s))
                # U[s] = max(A(s), key=lambda a: self.util_accao(s, a, Uant, modelo))
                delta = max(delta, abs(U[s] - Uant[s]))
            # se o delta for menor que o delta max
            if delta < self.__delta_max:
                break
        return U

    def util_accao(self, s, a, U, modelo):
        R = modelo.R
        T = modelo.T
        # print T(s, a)
        # print sum(p*(R(s, a, sn) + self.__gama*U[sn]) for p, sn in T(s, a))
        return sum(p*(R(s, a, sn) + self.__gama*U[sn]) for p, sn in T(s, a))

    def politica(self, U, modelo):
        S, A = modelo.S, modelo.A
        pol = {s: 0 for s in S()}
        for s in S():
            pol[s] = max(A(s), key=lambda a: self.util_accao(s, a, U, modelo))
        return pol

    def resolver(self, modelo):
        U = self.utilidade(modelo)
        pol = self.politica(U, modelo)
        return U, pol
