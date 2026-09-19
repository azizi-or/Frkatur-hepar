from abc import ABC, abstractmethod


class Beasiswa(ABC):

    def __init__(self, nama, bobot, kuota):
        self.nama = nama
        self.__bobot = bobot
        self.__kuota = kuota

    def get_bobot(self):
        return self.__bobot

    def set_bobot(self, bobot):
        self.__bobot = bobot

    def get_kuota(self):
        return self.__kuota

    def set_kuota(self, kuota):
        self.__kuota = kuota

    @abstractmethod
    def hitung_skor(self, pendaftar):
        pass