from lib.aprend_ref.memoria_aprend import MemoriaAprend


class MemoriaEsparsa(MemoriaAprend):

    @property
    def get_memoria(self):
        return self.__memoria

    def __init__(self, valor_omissao=0.0):
        self.__valor_omissao = valor_omissao
        self.__memoria = {}

    def actualizar(self, s, a, q):
        self.__memoria[(s, a)] = q

    def obter(self, s, a):
        return self.__memoria.get((s, a), self.__valor_omissao)
