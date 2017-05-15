from psa.psa5.accao import Mover
from lib.ecr.reaccao import Reaccao
from lib.ecr.resposta import Resposta


class AproximarDir(Reaccao):

    def __init__(self, direccao):
        self.__direccao = direccao
        self.__accao = Mover(direccao)

    def detectar_estimulo(self, percepcao):
        if percepcao[self.__direccao].alvo:
            return percepcao[self.__direccao].distancia

    def gerar_resposta(self, estimulo):
        prioridade = 1 / (1 + estimulo)
        return Resposta(self.__accao, prioridade)
