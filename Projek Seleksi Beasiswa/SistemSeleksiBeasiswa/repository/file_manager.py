import json
import csv
import os
import json
import csv
import os  # <-- Tambahkan modul os


class FileManager:

    @staticmethod
    def simpan_json(data, nama_file):
        # Otomatis buat folder jika foldernya belum ada
        os.makedirs(os.path.dirname(nama_file), exist_ok=True)

        with open(nama_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def simpan_csv(data, nama_file):
        # Otomatis buat folder jika foldernya belum ada
        os.makedirs(os.path.dirname(nama_file), exist_ok=True)

        if not data:
            return

        with open(nama_file, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

class FileManager:

    @staticmethod
    def simpan_json(data, nama_file):

        with open(nama_file, "w", encoding="utf-8") as file:

            json.dump(data, file, indent=4)

    @staticmethod
    def baca_json(nama_file):

        if not os.path.exists(nama_file):
            return []

        with open(nama_file, "r", encoding="utf-8") as file:

            return json.load(file)

    @staticmethod
    def simpan_csv(data, nama_file):

        with open(nama_file, "w", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Nama",
                "Umur",
                "IPK",
                "Penghasilan",
                "Prestasi",
                "Jenis Beasiswa",
                "Skor",
                "status"
            ])

            for d in data:
                writer.writerow([
                d["nama"],
                d["umur"],
                d["ipk"],
                d["penghasilan"],
                d["prestasi"],
                d["jenis"],
                d["skor"],
                d["status"]
            ])