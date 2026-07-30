from models.beasiswa import Beasiswa


class BeasiswaPrestasi(Beasiswa):

    def __init__(self):
        super().__init__(
            "Beasiswa Prestasi",
            40,
            5
        )

    def hitung_skor(self, pendaftar):

        skor = 0

        # IPK maksimal menyumbang 80 poin
        skor += pendaftar.ipk * 20

        # Prestasi
        if pendaftar.prestasi.lower() != "tidak ada":
            skor += 20

        return skor