class AgenteProspector(Agente):

    def __init__(self, controlo):
        self._controlo = controlo

    def executar(self):
        percepcao = self._percepcionar()
        accao = self._processar(percepcao)
        if accao is not None:
            self._actuar(accao)

    def _percepcionar(self):
        return self.sensor_multiplo.detectar()

    def _processar(self, percepcao):


    def _actuar(self):

