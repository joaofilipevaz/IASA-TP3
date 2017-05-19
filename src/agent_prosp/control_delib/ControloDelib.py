import psa.util.dirmov()
import psa.util.mover()
import psa.util.dist()
import psa.util.Mover(angulo, ang_abs = true)

import modelo_mundo


class ControloDelib:

    def __init__(self, planeador):
        self.__planeador = planeador

    def __reconsiderar(self):
        return self.__modelomundo.alterado

    def __deliberar(self):
        self.objectivo = "todos os alvos"


    def __planear(self):
        if self.objectivo:


    def __executar(self):

    def processar(self, percepcao):
        self._assimilar(percepcao)
        if self.__reconsiderar():
            self.__deliberar()
            self.__planear()
        return self.__executar()

    def _assimilar(self, per):
