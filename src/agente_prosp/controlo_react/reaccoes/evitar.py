from psa.psa5.actuador import FRT, ESQ, Rodar
from lib.ecr.resposta import Resposta
from lib.ecr.reaccao import Reaccao


class Evitar(Reaccao):
    def _detectar_estimulo(self, percepcao):
        return percepcao[FRT].contacto and percepcao[FRT].obstaculo

    def _gerar_resposta(self, estimulo):
        accao = Rodar(ESQ)
        return Resposta(accao)
