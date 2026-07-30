class Pendaftar:

    def __init__(
        self,
        nama,
        umur,
        ipk,
        penghasilan,
        prestasi,
        berkas_lengkap,
        jenis_beasiswa
    ):

        self.nama = nama
        self.umur = umur
        self.ipk = ipk
        self.penghasilan = penghasilan
        self.prestasi = prestasi
        self.berkas_lengkap = berkas_lengkap
        self.jenis_beasiswa = jenis_beasiswa

        self.skor = 0
        self.status = "Belum Dinilai"
        self.alasan = "-"

    def tampilkan(self):

        print("=" * 45)
        print(f"Nama              : {self.nama}")
        print(f"Umur              : {self.umur}")
        print(f"IPK               : {self.ipk}")
        print(f"Penghasilan       : Rp {self.penghasilan}")
        print(f"Prestasi          : {self.prestasi}")
        print(f"Berkas Lengkap    : {self.berkas_lengkap}")
        print(f"Jenis Beasiswa    : {self.jenis_beasiswa}")
        print(f"Skor              : {self.skor}")
        print(f"Status            : {self.status}")
        print(f"Alasan            : {self.alasan}")
        print("=" * 45)