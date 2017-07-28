from psa.psa5.accao import Mover
from psa.psa5.actuador import ESQ, DIR, FRT
from random import choice
from lib.ecr.comportamento import Comportamento
from lib.ecr.resposta import Resposta


class Explorar(Comportamento):

    def activar(self, percepcao):
        accao = choice([Mover(ESQ), Mover(FRT), Mover(DIR)])
        return Resposta(accao)
