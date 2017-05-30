from psa.util import dirmov
from psa.util import mover
from psa.util import dist
from psa.accao import Mover #(angulo, ang_abs = true)
from lib.plan.planeador import Planeador
from agente_prosp.controlo import Controlo
from agente_prosp.controlo_delib.modelo_mundo import ModeloMundo

class ControloDelib(Controlo):

    def __init__(self, planeador):
        self.__planeador = planeador
        self.__modelo_mundo = ModeloMundo.__init__()

    def __reconsiderar(self):
        return self.__modelo_mundo.alterado or self.__planeador.plano_pendente()

    def __deliberar(self):
        self.objectivo = "todos os alvos"

    def __planear(self):
        if self.objectivo:
            return self.__planeador.planear()

    def __executar(self):
        self.__planeador.obter_accao()

    def processar(self, percepcao):
        self.__assimilar(percepcao)
        if self.__reconsiderar():
            self.__deliberar()
            self.__planear()
        return self.__executar()

    def __assimilar(self, per):
        self.__modelo_mundo.actualizar(per)

