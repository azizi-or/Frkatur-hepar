import os
import json

from models.pendaftar import Pendaftar

from strategy.prestasi_strategy import PrestasiStrategy
from strategy.ekonomi_strategy import EkonomiStrategy
from strategy.afirmasi_strategy import AfirmasiStrategy
from strategy.kombinasi_strategy import KombinasiStrategy

from repository.file_manager import FileManager

from exceptions.berkas_error import BerkasTidakLengkapError
from exceptions.duplikasi_error import PendaftarDuplikatError


# ==========================
# Data Program
# ==========================

daftar_pendaftar = []
hasil_penilaian = []


# ==========================
# Auto-Load Data
# ==========================

def muat_data_otomatis():
    """Memuat data pendaftar otomatis dari file JSON saat program berjalan."""
    filepath = "data/penilaian.json"
    if not os.path.exists(filepath):
        return

    try:
        with open(filepath, "r") as file:
            data = json.load(file)
            for item in data:
                p = Pendaftar(
                    item["nama"],
                    item["umur"],
                    item["ipk"],
                    item["penghasilan"],
                    item["prestasi"],
                    True,
                    item["jenis"]
                )
                p.skor = item.get("skor", 0)
                p.status = item.get("status", "-")
                daftar_pendaftar.append(p)
        print(f"[System] Berhasil memuat {len(daftar_pendaftar)} data pendaftar dari file.")
    except Exception as e:
        print(f"[System] Gagal memuat data lama: {e}")


# ==========================
# Memilih Strategy
# ==========================

def pilih_strategy(jenis):
    if jenis.lower() == "prestasi":
        return PrestasiStrategy()
    elif jenis.lower() == "ekonomi":
        return EkonomiStrategy()
    elif jenis.lower() == "afirmasi":
        return AfirmasiStrategy()
    else:
        return KombinasiStrategy()


# ==========================
# 1. Tambah Pendaftar
# ==========================

def tambah_pendaftar():
    try:
        print("\n===== PENDAFTARAN =====")

        nama = input("Nama : ").strip()
        if not nama:
            print("tolong isi seuai permintaaan yang ada di form")
            return

        umur = int(input("Umur : "))
        
        # Pengecekan Batasan Usia (15 - 35 Tahun)
        if umur < 15 or umur > 35:
            print("umur tidak sesuai")
            return

        ipk = float(input("IPK : "))
        penghasilan = int(input("Penghasilan Orang Tua : "))
        prestasi = input("Prestasi : ").strip()
        berkas = input("Berkas lengkap? (y/t) : ").strip().lower()
        jenis = input("Jenis Beasiswa (Prestasi/Ekonomi/Afirmasi) : ").strip().capitalize()

        # Validasi Pilihan Jenis Beasiswa
        if jenis not in ["Prestasi", "Ekonomi", "Afirmasi"]:
            print("tolong isi seuai permintaaan yang ada di form")
            return

        # Cek Duplikasi Nama
        for p in daftar_pendaftar:
            if p.nama.lower() == nama.lower():
                raise PendaftarDuplikatError()

        if ipk < 3.00:
            print("IPK tidak memenuhi syarat.")
            return

        if berkas != "y":
            raise BerkasTidakLengkapError()

        # Buat Objek Pendaftar
        pendaftar = Pendaftar(
            nama,
            umur,
            ipk,
            penghasilan,
            prestasi,
            True,
            jenis
        )

        # Hitung Skor Berdasarkan Strategy
        strategy = pilih_strategy(jenis)
        skor = strategy.hitung(pendaftar)
        pendaftar.skor = skor

        daftar_pendaftar.append(pendaftar)
        print("\nPendaftar berhasil ditambahkan.")

    except ValueError:
        print("tolong isi seuai permintaaan yang ada di form")

    except BerkasTidakLengkapError as e:
        print(e)

    except PendaftarDuplikatError as e:
        print(e)


# ==========================
# 2. Tampilkan Ranking
# ==========================

def tampilkan_ranking():
    if len(daftar_pendaftar) == 0:
        print("\nBelum ada pendaftar.")
        return

    # Urutkan berdasarkan skor tertinggi
    ranking = sorted(
        daftar_pendaftar,
        key=lambda x: x.skor,
        reverse=True
    )

    hasil_penilaian.clear()

    print("\n========== HASIL SELEKSI ==========\n")

    kuota = {
        "Prestasi": 5,
        "Ekonomi": 10,
        "Afirmasi": 3
    }

    jumlah_per_jenis = {
        "Prestasi": 0,
        "Ekonomi": 0,
        "Afirmasi": 0
    }

    for i, p in enumerate(ranking, start=1):

        if jumlah_per_jenis.get(p.jenis_beasiswa, 0) < kuota.get(p.jenis_beasiswa, 0):
            jumlah_per_jenis[p.jenis_beasiswa] += 1
            p.status = "LULUS"
            p.alasan = "Masuk dalam kuota"
        else:
            p.status = "TIDAK LULUS"
            p.alasan = "Kuota penuh"

        print(f"{i}. {p.nama}")
        print(f"   Umur           : {p.umur} tahun")
        print(f"   Jenis Beasiswa : {p.jenis_beasiswa}")
        print(f"   Skor           : {p.skor:.2f}")
        print(f"   Status         : {p.status}")
        print(f"   Alasan         : {p.alasan}")
        print()

        hasil_penilaian.append({
            "nama": p.nama,
            "umur": p.umur,
            "ipk": p.ipk,
            "penghasilan": p.penghasilan,
            "prestasi": p.prestasi,
            "jenis": p.jenis_beasiswa,
            "skor": p.skor,
            "status": p.status,
            "alasan": p.alasan
        })


# ==========================
# 3. Cari Pendaftar (Fitur Baru)
# ==========================

def cari_pendaftar():
    if len(daftar_pendaftar) == 0:
        print("\nBelum ada pendaftar.")
        return

    kata_kunci = input("\nMasukkan Nama Pendaftar yang dicari: ").strip().lower()
    ditemukan = [p for p in daftar_pendaftar if kata_kunci in p.nama.lower()]

    if not ditemukan:
        print("Data pendaftar tidak ditemukan.")
        return

    print(f"\n--- Ditemukan {len(ditemukan)} Pendaftar ---")
    for p in ditemukan:
        print(f"• Nama: {p.nama} | Jenis: {p.jenis_beasiswa} | Skor: {p.skor:.2f} | Status: {getattr(p, 'status', 'Belum Diseleksi')}")


# ==========================
# 4. Hapus Pendaftar (Fitur Baru)
# ==========================

def hapus_pendaftar():
    if len(daftar_pendaftar) == 0:
        print("\nBelum ada pendaftar.")
        return

    nama = input("\nMasukkan Nama Pendaftar yang ingin dihapus: ").strip().lower()
    
    for p in daftar_pendaftar:
        if p.nama.lower() == nama:
            daftar_pendaftar.remove(p)
            print(f"\nPendaftar '{p.nama}' berhasil dihapus.")
            return

    print("Data pendaftar tidak ditemukan.")


# ==========================
# 5. Simpan Hasil
# ==========================

def simpan_hasil():
    if len(hasil_penilaian) == 0:
        print("Belum ada hasil seleksi. Silakan jalankan menu 'Tampilkan Ranking' terlebih dahulu.")
        return

    FileManager.simpan_json(
        hasil_penilaian,
        "data/penilaian.json"
    )

    FileManager.simpan_csv(
        hasil_penilaian,
        "data/hasil_seleksi.csv"
    )

    print("Hasil berhasil disimpan.")


# ==========================
# Menu Utama
# ==========================

def menu():
    # Otomatis muat data lama begitu program dibuka
    muat_data_otomatis()

    while True:
        print("\n===================================")
        print("   SISTEM SELEKSI BEASISWA")
        print("===================================")
        print("1. Tambah Pendaftar")
        print("2. Tampilkan Ranking & Seleksi")
        print("3. Cari Pendaftar")
        print("4. Hapus Pendaftar")
        print("5. Simpan Hasil ke File")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ").strip()

        if pilihan == "1":
            tambah_pendaftar()
        elif pilihan == "2":
            tampilkan_ranking()
        elif pilihan == "3":
            cari_pendaftar()
        elif pilihan == "4":
            hapus_pendaftar()
        elif pilihan == "5":
            simpan_hasil()
        elif pilihan == "6":
            print("\nTerima kasih telah menggunakan program.")
            break
        else:
            print("\nPilihan tidak valid!")


# ==========================
# Program Dimulai
# ==========================

if __name__ == "__main__":
    menu()