
import psa
import sys

sys.path.append(".../agente_prosp")
sys.path.append(".../lib")
from agente_prosp import agente_prosp
from agente_prosp import AgenteProspector
from agente_prosp.controlo_react import controlo_react
from agente_prosp.controlo_react.reaccoes.recolher import Recolher as Comportamento
psa.iniciar("amb/amb1.class")
psa.executar(AgenteProspector(controlo_react(Comportamento)))