from lib.ecr.comport_comp import ComportComp


class Prioridade(ComportComp):

    def selecionar_resposta(self, respostas):
        if respostas:
            return max(respostas, key=lambda resp: resp.prioridade)
