
from agent_prosp import controlo



class ControloReact(controlo):
    def __init__(self, recolher):
        self.__comportamento = recolher

    def processar(self, percepcao):
        return self.__comportamento.activar(percepcao).accao
