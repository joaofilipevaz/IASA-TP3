from psa.psa5.actuador import ESQ, DIR, FRT, Mover
from lib.ecr.reaccao import Reaccao
from lib.ecr.resposta import Resposta


class Contornar(Reaccao):
    def detectar_estimulo(self, percepcao):
        return (percepcao[ESQ].contacto and percepcao[ESQ].obstaculo) or \
               (percepcao[DIR].contacto and percepcao[DIR].obstaculo)

    def gerar_resposta(self, estimulo):
        accao = Mover(FRT)
        return Resposta(accao)
