<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mini Project 1 - Product Information System</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f9f9f9;
        }
        h2 {
            color: #333;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            background-color: #fff;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 10px 12px;
            text-align: left;
        }
        th {
            background-color: #2c3e50;
            color: white;
        }
        /* Style indikator stok kritis (< 3) */
        .stok-kritis {
            background-color: #ffd2d2; /* Warna merah muda */
            color: #8b0000;
            font-weight: bold;
        }
        .total-box {
            padding: 15px 20px;
            background-color: #e8f4f8;
            border: 1px solid #b6e0fe;
            display: inline-block;
            border-radius: 6px;
            font-size: 16px;
            color: #1b4965;
        }
    </style>
</head>
<body>

    <h2>Product Information System (Desain Konseptual)</h2>

    <!-- PRESENTATION LAYER: Tabel HTML untuk menampilkan data -->
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Nama Produk</th>
                <th>Kategori</th>
                <th>Harga</th>
                <th>Stok</th>
                <th>Deskripsi</th>
            </tr>
        </thead>
        <tbody>
            <!-- DATA LAYER & PROCESSING LAYER: 10 Produk -->
            <tr>
                <td>1</td>
                <td>Laptop Asus Vivobook</td>
                <td>Elektronik</td>
                <td>Rp 8.500.000</td>
                <td>15</td>
                <td>Laptop kerja dan kuliah ringan</td>
            </tr>
            <tr class="stok-kritis">
                <td>2</td>
                <td>Mouse Wireless Logitech</td>
                <td>Aksesori</td>
                <td>Rp 180.000</td>
                <td>2</td>
                <td>Mouse optik responsif (Stok Kritis)</td>
            </tr>
            <tr>
                <td>3</td>
                <td>Keyboard Mechanical RGB</td>
                <td>Aksesori</td>
                <td>Rp 450.000</td>
                <td>8</td>
                <td>Switch biru hotswap</td>
            </tr>
            <tr>
                <td>4</td>
                <td>Monitor LED 24 Inch</td>
                <td>Elektronik</td>
                <td>Rp 1.750.000</td>
                <td>12</td>
                <td>Panel IPS Full HD 75Hz</td>
            </tr>
            <tr class="stok-kritis">
                <td>5</td>
                <td>Webcam Full HD 1080p</td>
                <td>Aksesori</td>
                <td>Rp 320.000</td>
                <td>1</td>
                <td>Lensa mikrofon built-in (Stok Kritis)</td>
            </tr>
            <tr>
                <td>6</td>
                <td>Headset Gaming 7.1</td>
                <td>Audio</td>
                <td>Rp 350.000</td>
                <td>20</td>
                <td>Surround sound bass mantap</td>
            </tr>
            <tr>
                <td>7</td>
                <td>Flashdisk 64GB USB 3.0</td>
                <td>Penyimpanan</td>
                <td>Rp 85.000</td>
                <td>45</td>
                <td>Kecepatan transfer tinggi</td>
            </tr>
            <tr>
                <td>8</td>
                <td>External SSD 500GB</td>
                <td>Penyimpanan</td>
                <td>Rp 850.000</td>
                <td>10</td>
                <td>Desain portabel dan tahan guncangan</td>
            </tr>
            <tr class="stok-kritis">
                <td>9</td>
                <td>Stand Laptop Alumunium</td>
                <td>Aksesori</td>
                <td>Rp 125.000</td>
                <td>2</td>
                <td>Ergonomis dan dapat dilipat (Stok Kritis)</td>
            </tr>
            <tr>
                <td>10</td>
                <td>Printer Inktank RGB</td>
                <td>Elektronik</td>
                <td>Rp 2.100.000</td>
                <td>6</td>
                <td>Cetak hemat dan kapasitas besar</td>
            </tr>
        </tbody>
    </table>

    <!-- PROCESSING LAYER LOGIC: Total Nilai Aset Gudang -->
    <!-- Kalkulasi total: (8.5jt*15) + (180rb*2) + (450rb*8) + (1.75jt*12) + (320rb*1) + (350rb*20) + (85rb*45) + (850rb*10) + (125rb*2) + (2.1jt*6) -->
    <div class="total-box">
        <strong>Total Nilai Aset Gudang:</strong> Rp 189.205.000
    </div>

</body>
</html>