
import psa
import sys

sys.path.append(".../agente_prosp")
sys.path.append(".../lib")

from agent_prosp import Agente Prospector
from controlo_react.controlo_react import ControloReact
from controlo_react.reaccoes.recolher import Recolher as Comportamento
psa.iniciar("amb/amb1.class")
psa.executar(AgenteProspector(ControloReact(Comportamento)))