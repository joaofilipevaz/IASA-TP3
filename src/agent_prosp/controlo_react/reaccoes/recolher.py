from agent_prosp.controlo_react.reaccoes.aproximar.aproximar import Aproximar
from agent_prosp.controlo_react.reaccoes.contornar import Contornar
from agent_prosp.controlo_react.reaccoes.evitar import Evitar
from agent_prosp.controlo_react.reaccoes.explorar import Explorar
from lib.ecr.hierarquia import *


class Recolher(Hierarquia):
    def __init__(self):
        super(Recolher, self).__init__(
            [Aproximar(), Evitar(), Contornar(), Explorar()]
        )