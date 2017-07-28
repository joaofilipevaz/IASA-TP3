import psa
import sys

sys.path.append(".../agente_prosp")
sys.path.append(".../lib")

from agente_prosp.agente_prosp import AgenteProspector
from agente_prosp.controlo_react.controlo_react import ControloReact
from agente_prosp.controlo_react.reaccoes.recolher import Recolher as Comportamento

psa.iniciar("amb/amb1.das")
psa.executar(AgenteProspector(ControloReact(Comportamento())))
