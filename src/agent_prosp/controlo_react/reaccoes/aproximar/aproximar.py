from agent_prosp.controlo_react.reaccoes.aproximar.aproximar_dir import AproximarDir
from lib.ecr.prioridade import Prioridade
from psa.psa5.actuador import FRT, DIR, ESQ


class Aproximar(Prioridade):

    def __init__(self):
        super(Aproximar, self).__init__(
            [AproximarDir(FRT), AproximarDir(ESQ), AproximarDir(DIR)]
        )
