from lib.pdm.modelo_pdm import ModeloPDM

class Pdm(ModeloPDM):

    def __init__(self, gama, delta_max):
        self.__gama = gama
        self.__delta_max = delta_max



    def utilidade(self, modelo):
        S = modelo.S
        A = modelo.A
        U = { s:0 for s in S()}
        while True:
            Uant = U.copy()
            delta = 0
            for s in S():
                max()

