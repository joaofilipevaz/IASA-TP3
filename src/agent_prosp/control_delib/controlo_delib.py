from psa.util import dirmov
import psa.util.mover()
import psa.util.dist()
from psa.util import Mover(angulo, ang_abs = true)
from lib.plan.planeador import Planeador

import modelo_mundo
from agent_prosp.controlo import Controlo

class ControloDelib(Controlo):

    def __init__(self, planeador):
        self.__planeador = planeador

    def __reconsiderar(self):
        return self.__modelo_mundo.ModeloMundo.alterado() or self.__planeador.plano_pendente()

    def __deliberar(self):
        self.objectivo = "todos os alvos"

    def __planear(self):
        if self.objectivo:
            return self.__planeador.planear()

    def __executar(self):
        self.__planeador.obter_accao()

    def processar(self, percepcao):
        self._assimilar(percepcao)
        if self.__reconsiderar():
            self.__deliberar()
            self.__planear()
        return self.__executar()

    def _assimilar(self, per):
