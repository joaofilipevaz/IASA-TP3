from lib.aprend_ref.aprend_ref import AprendRef


class AprendQ(AprendRef):

    def __init__(self, mem_aprend, sel_accao, alfa, gama):
        super(AprendQ, self).__init__(mem_aprend, sel_accao)
        self._alfa = alfa
        self._gama = gama
        self._mem_aprend = mem_aprend
        self._sel_accao = sel_accao

    def aprender(self, s, a, r, sn):
        an = self._sel_accao.max_accao(s)
        qsa = self._mem_aprend.obter(s, a)
        qsnan = self._mem_aprend.obter(sn, an)
        q = self._mem_aprend.actualizar(s, a, qsnan)

