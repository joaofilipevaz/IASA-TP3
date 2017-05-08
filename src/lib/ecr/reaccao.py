def Reaccao(Comportamento):

    def activar(self, percepcao):
        estimulo = self.detectar_estimulo(percepcao)
        if estimulo is not None and estimulo is not False:
            resposta = self.gerar_resposta(estimulo)
            return resposta

    def _gerar_resposta(self, estimulo):
        abstract

    def _detectar_estimulo(self, percepcao):
        abstract
