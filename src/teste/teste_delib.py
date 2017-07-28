import psa
import sys

sys.path.append("../agente_prosp")
sys.path.append("../lib")
sys.path.append("../amb")

from agente_prosp.agente_prosp import AgenteProspector
from agente_prosp.controlo_delib.controlo_delib import ControloDelib
from lib.plan.plan_pee.plan_pee import PlanPEE
from pee.melhorprim.procura_aa import ProcuraAA
from pee.melhorprim.procura_sofrega import ProcuraSofrega
from pee.melhorprim.procura_custo_unif import ProcuraCustoUnif
from pee.larg.procura_larg import ProcuraLarg
from pee.prof.procura_prof import ProcuraProf
from pee.prof.procura_prof_iter import ProcuraProfIter

psa.iniciar("amb/amb1.das")
#psa.executar(AgenteProspector(ControloDelib(PlanPEE(ProcuraAA()))))
#psa.executar(AgenteProspector(ControloDelib(PlanPEE(ProcuraCustoUnif()))))
#psa.executar(AgenteProspector(ControloDelib(PlanPEE(ProcuraSofrega()))))

#psa.executar(AgenteProspector(ControloDelib(PlanPEE(ProcuraLarg()))))
#psa.executar(AgenteProspector(ControloDelib(PlanPEE(ProcuraProf()))))
psa.executar(AgenteProspector(ControloDelib(PlanPEE(ProcuraProfIter()))))