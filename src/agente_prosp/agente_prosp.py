from psa.agente import Agente


class AgenteProspector(Agente):

    def __init__(self, controlo):
        self.__controlo = controlo

    def executar(self):
        percepcao = self.__percepcionar()
        accao = self.__processar(percepcao)
        if accao is not None:
            self.__actuar(accao)

    def __percepcionar(self):
        return self.sensor_multiplo.detectar()

    def __processar(self, percepcao):
        return self.__controlo.processar(percepcao)

    def __actuar(self, accao):
        return self.actuador.actuar(accao)
