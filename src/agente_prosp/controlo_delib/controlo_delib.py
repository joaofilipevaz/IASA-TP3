from agente_prosp.controlo import Controlo
from agente_prosp.controlo_delib.modelo_mundo import ModeloMundo
import psa.util


class ControloDelib(Controlo):

    def __init__(self, planeador):
        self.__planeador = planeador
        self.__modelo_mundo = ModeloMundo()
        self.__objectivos = []

    def __reconsiderar(self):
        return self.__modelo_mundo.alterado or self.__planeador.plano_pendente() or self.__objectivos

    def __deliberar(self):
        self.__objectivos = [estado for estado in self.__modelo_mundo.estados()
                          if self.__modelo_mundo.obter_elem(estado) == "alvo"]

    def __planear(self):
        if self.__objectivos:
            return self.__planeador.planear(self.__modelo_mundo, self.__modelo_mundo.estado, self.__objectivos)
        else:
            self.__planeador.terminar_plano()

    def __executar(self):
        return self.__planeador.obter_accao(self.__modelo_mundo.estado)

    def processar(self, percepcao):
        self.__assimilar(percepcao)
        if self.__reconsiderar():
            self.__deliberar()
            self.__planear()
        self.mostrar(self.__modelo_mundo.estado)
        return self.__executar()

    def __assimilar(self, per):
        self.__modelo_mundo.actualizar(per)

    def mostrar(self, s):
        vis = psa.vis(1)
        vis.limpar()
        self.__planeador.mostrar(vis, s)
        self.__modelo_mundo.mostrar(vis)
