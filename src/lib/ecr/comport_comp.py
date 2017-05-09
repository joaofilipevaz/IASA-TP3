import abc
from lib.ecr.comportamento import Comportamento


class ComportComp(Comportamento):

    def __init__(self, comportamentos):
        self._comportamentos = comportamentos

    def activar(self, percepcao):
        respostas = []
        for comportamento in self._comportamentos:
            resposta = comportamento.activar(percepcao)
            if resposta:
                respostas.append(resposta)
        if respostas:
            return self.selecionar_resposta(respostas)

    @abc.abstractmethod
    def selecionar_resposta(self, respostas):
        """da a resposta"""
