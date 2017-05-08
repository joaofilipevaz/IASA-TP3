

class Prioridade(Comportamento):

    def selecionar_respostas(self, respostas):
        if respostas:
            return max(respostas, key=lambda resp: resp.prioridade)