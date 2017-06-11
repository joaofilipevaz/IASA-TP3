from lib.aprend_ref.memoria_aprend import MemoriaAprend


class MemoriaEsparsa(MemoriaAprend):

    def __init__(self, valor_omissao=0.0):
        self.__valor_omissao = valor_omissao

    @classmethod
    def MemoriaEsparsa(cls):
        return cls

    def actualizar(self, s, a, q):
        pass

    def obter(self, s, a):
        pass
