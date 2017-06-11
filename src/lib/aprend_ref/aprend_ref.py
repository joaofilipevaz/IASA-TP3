import abc


class AprendRef:
    __metaclass__ = abc.ABCMeta

    def __init__(self, mem_aprend, sel_accao):
        self._mem_aprend = mem_aprend
        self._sel_accao = sel_accao

    @abc.abstractmethod
    def aprender(self, s, a, r, sn):
        """void"""
