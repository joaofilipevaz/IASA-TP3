import psa
import sys
from lib.ecr.comportamento import Comportamento

sys.path.append(".../agente_prosp")
sys.path.append(".../lib")
from agent_prosp import agente_prosp
from agent_prosp.agente_prosp import AgenteProspector
from agent_prosp.control_delib import controlo_delib
#from agent_prosp.control_delib import Recolher as Comportamento
psa.iniciar("amb/amb1.class")
psa.executar(AgenteProspector(controlo_delib(Comportamento)))