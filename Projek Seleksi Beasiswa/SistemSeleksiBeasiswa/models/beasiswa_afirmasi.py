from models.beasiswa import Beasiswa


class BeasiswaAfirmasi(Beasiswa):

    def __init__(self):
        super().__init__(
            "Beasiswa Afirmasi",
            30,
            3
        )

    def hitung_skor(self, pendaftar):

        skor = 0

        skor += pendaftar.ipk * 15

        if pendaftar.umur <= 21:
            skor += 30

        if pendaftar.prestasi.lower() != "tidak ada":
            skor += 10

        return skor