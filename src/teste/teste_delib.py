import psa
import sys

sys.path.append("../agente_prosp")
sys.path.append("../lib")

from agente_prosp.agente_prosp import AgenteProspector
from agente_prosp.controlo_delib.controlo_delib import ControloDelib
from lib.plan.plan_pee.plan_pee import PlanPEE
from pee.melhorprim.procura_aa import ProcuraAA

psa.iniciar("amb/amb5.das")
psa.executar(AgenteProspector(ControloDelib(PlanPEE(ProcuraAA()))))
