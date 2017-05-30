from agente_prosp.controlo import Controlo


class ControloReact(Controlo):
    def __init__(self, comportamento):
        self.__comportamento = comportamento

    def processar(self, percepcao):
        return self.__comportamento.activar(percepcao).accao
