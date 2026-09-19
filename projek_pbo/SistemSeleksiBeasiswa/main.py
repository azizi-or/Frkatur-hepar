from models.pendaftar import Pendaftar

# Menyimpan data sementara
daftar_pendaftar = []


def tampil_menu():
    print("\n" + "=" * 50)
    print("      SISTEM SELEKSI BEASISWA")
    print("=" * 50)
    print("1. Tambah Pendaftar")
    print("2. Lihat Data Pendaftar")
    print("3. Keluar")
    print("=" * 50)


while True:

    tampil_menu()

    pilihan = input("Masukkan pilihan : ")

    if pilihan == "1":

        print("\n=== INPUT DATA PENDAFTAR ===")

        nama = input("Nama                : ")
        umur = int(input("Umur                : "))
        ipk = float(input("IPK                 : "))
        penghasilan = int(input("Penghasilan Orang Tua : "))
        prestasi = input("Prestasi (atau ketik 'Tidak Ada') : ")

        print("\nJenis Beasiswa")
        print("1. Prestasi")
        print("2. Ekonomi")
        print("3. Afirmasi")

        pilih = input("Pilih : ")

        if pilih == "1":
            jenis = "Prestasi"
        elif pilih == "2":
            jenis = "Ekonomi"
        elif pilih == "3":
            jenis = "Afirmasi"
        else:
            print("Pilihan tidak valid!")
            continue

        pendaftar = Pendaftar(
            nama,
            umur,
            ipk,
            penghasilan,
            prestasi,
            jenis
        )

        daftar_pendaftar.append(pendaftar)

        print("\nData berhasil ditambahkan!")

    elif pilihan == "2":

        if len(daftar_pendaftar) == 0:
            print("\nBelum ada data pendaftar.")

        else:

            print("\n===== DAFTAR PENDAFTAR =====")

            no = 1

            for p in daftar_pendaftar:

                print(f"\nPendaftar {no}")

                p.tampilkan()

                no += 1

    elif pilihan == "3":

        print("\nTerima kasih telah menggunakan program.")
        break

    else:

        print("\nMenu tidak tersedia!")