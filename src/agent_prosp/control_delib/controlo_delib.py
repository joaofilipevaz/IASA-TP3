import psa.util.dirmov()
import psa.util.mover()
import psa.util.dist()
import psa.util.Mover(angulo, ang_abs = true)

import modelo_mundo
from agent_prosp import controlo

class ControloDelib(controlo.Controlo):

    def __init__(self, planeador):
        self.__planeador = planeador

    def __reconsiderar(self):
        return self.__modelo_mundo.ModeloMundo.alterado() or self.__planeador.plano_pendente()

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
