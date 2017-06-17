import psa

from psa.psa5.agente import Agente
from psa.psa5.accao import Avancar

class AgenteDeTeste(Agente):
    def executar(self):
        self.actuador.actuar(Avancar())

psa.iniciar("amb/amb1.das")
psa.executar(AgenteDeTeste())
