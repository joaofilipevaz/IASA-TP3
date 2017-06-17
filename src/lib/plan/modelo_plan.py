import abc

class ModeloPlan:
    _metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def estados(self):
        "abstract"

    @abc.abstractmethod
    def operadores(self):
        "abstract"
