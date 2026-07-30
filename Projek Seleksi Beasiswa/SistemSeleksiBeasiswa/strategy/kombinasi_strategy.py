from strategy.strategy import Strategy


class KombinasiStrategy(Strategy):

    def hitung(self, pendaftar):

        skor = 0

        skor += pendaftar.ipk * 20

        if pendaftar.prestasi.lower() != "tidak ada":
            skor += 20

        if pendaftar.penghasilan <= 3000000:
            skor += 20

        if pendaftar.umur <= 22:
            skor += 10

        return skor