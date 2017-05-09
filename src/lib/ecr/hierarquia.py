from lib.ecr.comport_comp import ComportComp


class Hierarquia(ComportComp):

    def selecionar_resposta(self, respostas):
        if respostas:
            return respostas[0]