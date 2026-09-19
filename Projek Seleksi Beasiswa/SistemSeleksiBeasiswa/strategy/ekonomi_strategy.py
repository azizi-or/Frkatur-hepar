from strategy.strategy import Strategy


class EkonomiStrategy(Strategy):

    def hitung(self, pendaftar):

        skor = 0

        skor += pendaftar.ipk * 15

        if pendaftar.penghasilan <= 3000000:
            skor += 40

        elif pendaftar.penghasilan <= 5000000:
            skor += 20

        return skor