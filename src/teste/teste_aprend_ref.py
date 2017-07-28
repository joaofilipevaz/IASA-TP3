import psa
import sys

sys.path.append("../agente_prosp")
sys.path.append("../lib")

from agente_prosp.agente_prosp import AgenteProspector
from agente_prosp.controlo_aprend.controlo_aprend_ref import ControloAprendRef

psa.iniciar("amb/amb3.das", alvo_ini=True)
psa.executar(AgenteProspector(ControloAprendRef()))
