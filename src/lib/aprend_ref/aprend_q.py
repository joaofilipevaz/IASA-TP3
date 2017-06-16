from lib.aprend_ref.aprend_ref import AprendRef


class AprendQ(AprendRef):

    def __init__(self, mem_aprend, sel_accao, alfa, gama):
        super(AprendQ, self).__init__(mem_aprend, sel_accao)
        self._alfa = alfa
        self._gama = gama

    def aprender(self, s, a, r, sn):
        an = sel_accao.maxaccao(s,a)
        qsa = self._mem_aprend.obter(s, a)
        qsnan = mem_aprend.obter(sn, an)
        q = actualizar(s,a,q)

