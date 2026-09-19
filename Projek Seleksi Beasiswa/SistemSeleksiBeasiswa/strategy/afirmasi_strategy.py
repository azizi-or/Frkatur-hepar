from strategy.strategy import Strategy


class AfirmasiStrategy(Strategy):

    def hitung(self, pendaftar):

        skor = 0

        skor += pendaftar.ipk * 15

        if pendaftar.umur <= 21:
            skor += 30

        if pendaftar.prestasi.lower() != "tidak ada":
            skor += 10

        return skor