class PendaftarDuplikatError(Exception):
    def __init__(self, pesan="Pendaftar sudah terdaftar!"):
        self.pesan = pesan
        super().__init__(self.pesan)