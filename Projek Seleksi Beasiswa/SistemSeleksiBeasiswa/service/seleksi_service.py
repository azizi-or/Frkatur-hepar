from models.beasiswa_prestasi import BeasiswaPrestasi
from models.beasiswa_ekonomi import BeasiswaEkonomi
from models.beasiswa_afirmasi import BeasiswaAfirmasi


class SeleksiService:

    def __init__(self):
        self.daftar_beasiswa = {
            "Prestasi": BeasiswaPrestasi(),
            "Ekonomi": BeasiswaEkonomi(),
            "Afirmasi": BeasiswaAfirmasi()
        }

    def hitung_skor(self, pendaftar):

        beasiswa = self.daftar_beasiswa.get(
            pendaftar.jenis_beasiswa
        )

        if beasiswa:
            return beasiswa.hitung_skor(pendaftar)

        return 0