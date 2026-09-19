from models.beasiswa import Beasiswa


class BeasiswaEkonomi(Beasiswa):

    def __init__(self):
        super().__init__(
            "Beasiswa Ekonomi",
            35,
            10
        )

    def hitung_skor(self, pendaftar):

        skor = 0

        skor += pendaftar.ipk * 15

        if pendaftar.penghasilan <= 3000000:
            skor += 40

        elif pendaftar.penghasilan <= 5000000:
            skor += 20

        return skor