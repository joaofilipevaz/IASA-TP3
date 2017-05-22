
import psa
import sys

sys.path.append(".../agente_prosp")
sys.path.append(".../lib")
from agent_prosp import agente_prosp
from agent_prosp import AgenteProspector
from agent_prosp.controlo_react import controlo_react
from agent_prosp.controlo_react.reaccoes.recolher import Recolher as Comportamento
psa.iniciar("amb/amb1.class")
psa.executar(AgenteProspector(controlo_react(Comportamento)))