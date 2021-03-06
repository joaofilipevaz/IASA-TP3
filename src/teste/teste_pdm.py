import psa
import sys

sys.path.append("../agente_prosp")
sys.path.append("../lib")

from agente_prosp.agente_prosp import AgenteProspector
from agente_prosp.controlo_delib.controlo_delib import ControloDelib
from lib.plan.plan_pdm.plan_pdm import PlanPDM

psa.iniciar("amb/amb1.das")
psa.executar(AgenteProspector(ControloDelib(PlanPDM())))