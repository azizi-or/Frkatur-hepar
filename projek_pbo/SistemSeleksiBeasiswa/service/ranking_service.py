class RankingService:

    def ranking(self, daftar_pendaftar):

        return sorted(
            daftar_pendaftar,
            key=lambda x: x.skor,
            reverse=True
        )

    def tampilkan(self, daftar):

        print("\n========== HASIL RANKING ==========\n")

        nomor = 1

        for p in daftar:

            print(f"{nomor}. {p.nama}")
            print(f"   Jenis Beasiswa : {p.jenis_beasiswa}")
            print(f"   Skor           : {p.skor}")
            print(f"   Status         : {p.status}")
            print(f"   Alasan         : {p.alasan}")
            print()

            nomor += 1