<?php
require_once 'products.php';
require_once 'functions.php';

$totalAset = hitungTotalNilaiStok($products);
?>

<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Product Information System</title>
</head>
<body>

    <h2>Daftar Produk</h2>

    <table border="1" cellpadding="8" cellspacing="0">
        <thead>
            <tr>
                <th>ID</th>
                <th>Nama</th>
                <th>Kategori</th>
                <th>Harga</th>
                <th>Stok</th>
                <th>Deskripsi</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach ($products as $p): ?>
                <!-- Kasih warna merah pada baris jika stok < 3 -->
                <tr <?= getRowClass($p['stok']); ?>>
                    <td><?= $p['id']; ?></td>
                    <td><?= $p['nama']; ?></td>
                    <td><?= $p['kategori']; ?></td>
                    <td>Rp <?= number_format($p['harga'], 0, ',', '.'); ?></td>
                    <td><?= $p['stok']; ?></td>
                    <td><?= $p['deskripsi']; ?></td>
                </tr>
            <?php endforeach; ?>
        </tbody>
    </table>

    <h3>Total Nilai Aset Gudang: Rp <?= number_format($totalAset, 0, ',', '.'); ?></h3>

</body>
</html>