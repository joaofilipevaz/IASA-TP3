from lib.aprend_ref.aprend_q import AprendQ


class AprendQE(AprendQ):

    def __init__(self, mem_aprend, sel_accao, alfa, gama, nsim):
        super(AprendQE, self).__init__(mem_aprend, sel_accao, alfa, gama)
        self._nsim = nsim

    def aprender(self, s, a, r, sn):
        pass

    def __memorizar_episodio(self, s, a, r, sn):
        pass

    def __simular(self):
        pass
