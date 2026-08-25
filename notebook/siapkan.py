"""Penyiapan bersama untuk notebook pendamping buku.

Beberapa bab melanjutkan contoh dari bab sebelumnya. Di dalam buku,
sambungannya dijelaskan lewat prosa, sehingga listingnya sendiri tidak
mengulang penyiapan datanya. Modul ini menyediakan penyiapan itu supaya
tiap notebook dapat dijalankan sendiri dari atas.

Angkanya sama persis dengan yang tercetak di buku.
"""
import numpy as np


def data_rumah():
    """Delapan pengamatan harga rumah, dipakai Bab 13 sampai 15."""
    luas = np.array([36., 45., 54., 60., 70., 80., 90., 100.])
    kamar = np.array([1., 2., 2., 3., 3., 3., 4., 4.])
    y = np.array([326.2, 391.4, 424.6, 469.9,
                  515.4, 553.1, 628.5, 680.7])
    return luas, kamar, y


def matriks_desain():
    """Matriks desain terstandardisasi beserta sasarannya, Bab 13 dan 14."""
    luas, kamar, y = data_rumah()
    X = np.column_stack([luas, kamar])
    n = len(y)
    mu, sd = X.mean(axis=0), X.std(axis=0)
    Z = (X - mu) / sd
    Xb = np.column_stack([np.ones(n), Z])
    return Xb, y


def riwayat_biaya(eta, iterasi=200):
    """Riwayat biaya gradient descent, dipakai grafik Bab 9."""
    Xb, y = matriks_desain()
    n = len(y)
    w = np.zeros(Xb.shape[1])
    catat = []
    for _ in range(iterasi):
        r = Xb @ w - y
        catat.append(float(r @ r) / n)
        w = w - eta * (2.0 / n) * (Xb.T @ r)
    return np.array(catat)


def medan_gauss(n=200, lebar=3.0):
    """Medan dua dimensi untuk contoh peta warna Bab 9."""
    x = np.linspace(-lebar, lebar, n)
    X, Y = np.meshgrid(x, x)
    return np.exp(-(X ** 2 + Y ** 2))


def kue_tiga_bulan():
    """produk, trans, g dari data penjualan tiga bulan, Bab 10 dan 11."""
    from data_kue import gabung
    return gabung()


def kue_setahun():
    """produk, df dari data penjualan setahun, Bab 11."""
    from data_kue import setahun
    return setahun()


def kue_diperkaya():
    """Data diperkaya untuk studi kasus Bab 16 dan 17."""
    import data_kue2
    for nama in ("bangkitkan", "muat", "bangun", "data"):
        f = getattr(data_kue2, nama, None)
        if callable(f):
            return f()
    raise RuntimeError("fungsi pembangkit tidak ditemukan di data_kue2")
