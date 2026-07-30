from abc import ABC, abstractmethod

class Strategy(ABC):

    @abstractmethod
    def hitung(self, pendaftar):
        pass