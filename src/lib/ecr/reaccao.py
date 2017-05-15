import abc


def Reaccao(comportamento):

    def activar(self, percepcao):
        estimulo = self.detectar_estimulo(percepcao)
        if estimulo is not None and estimulo is not False:
            resposta = self.gerar_resposta(estimulo)
            return resposta

    @abc.abstractmethod
    def _gerar_resposta(self, estimulo):
        """Resposta"""

    @abc.abstractmethod
    def _detectar_estimulo(self, percepcao):
        """Estimulo"""
