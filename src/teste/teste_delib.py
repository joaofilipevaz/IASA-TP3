import psa
import sys

sys.path.append("../agente_prosp")
sys.path.append("../lib")

from agente_prosp import AgenteProspector
from agent_prosp.control_delib.controlo_delib import ControloDelib
from plan.plan_pee.PlanPEE import PlanPEE
from pee.melhorprim.procura_aa import ProcuraAA

psa.iniciar("amb/amb1.class")
psa.executar(AgenteProspector(ControloDelib(PlanPEE(ProcuraAA()))))
