class BerkasTidakLengkapError(Exception):
    def __init__(self, pesan="Berkas pendaftar belum lengkap!"):
        self.pesan = pesan
        super().__init__(self.pesan)