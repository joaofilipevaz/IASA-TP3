from agente_prosp.controlo_react.reaccoes.aproximar.aproximar_dir import AproximarDir
from lib.ecr.prioridade import Prioridade
from psa.psa5.actuador import DIR, ESQ, FRT


class Aproximar(Prioridade):

    def __init__(self):
        super(Aproximar, self).__init__(
            [AproximarDir(FRT), AproximarDir(ESQ), AproximarDir(DIR)]
        )
