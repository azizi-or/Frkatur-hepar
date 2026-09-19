from strategy.strategy import Strategy


class PrestasiStrategy(Strategy):

    def hitung(self, pendaftar):

        skor = 0

        skor += pendaftar.ipk * 20

        if pendaftar.prestasi.lower() != "tidak ada":
            skor += 40

        if pendaftar.umur <= 22:
            skor += 10

        return skor