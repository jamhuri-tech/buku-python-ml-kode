"""Data transaksi diperkaya untuk studi kasus Bab 15.

Data ini sintetis. Strukturnya sengaja dibangun agar diketahui
kebenarannya, sehingga hasil model dapat diperiksa terhadap mekanisme
pembangkitnya. Data nyata tidak sebersih ini.
"""
import numpy as np
import pandas as pd

PRODUK = pd.DataFrame({
    "produk": ["Nastar", "Kastengel", "Putri Salju",
               "Brownies", "Bolu Pandan", "Lapis Legit"],
    "kategori": ["kering", "kering", "kering",
                 "basah", "basah", "basah"],
    "harga": [85000, 95000, 78000, 45000, 40000, 120000],
})

# efek tetap yang dibangun ke dalam data (kebenaran yang diketahui)
EFEK_PRODUK = {"Nastar": 1.15, "Kastengel": 1.20, "Putri Salju": 1.00,
               "Brownies": 0.95, "Bolu Pandan": 0.90, "Lapis Legit": 0.70}
EFEK_KANAL = {"toko": 1.00, "online": 1.10, "reseller": 2.30}
EFEK_HARI = {0: 0.95, 1: 0.90, 2: 0.95, 3: 1.00,
             4: 1.20, 5: 1.45, 6: 1.30}          # 0=Senin
EFEK_PROMO = 1.55
EFEK_LEBARAN = {"kering": 2.60, "basah": 1.15}


def bangkitkan(seed=2026):
    rng = np.random.default_rng(seed)
    hari_semua = pd.date_range("2025-02-01", "2026-01-31", freq="D")
    baris = []

    for tgl in hari_semua:
        # Lebaran 2025 jatuh akhir Maret; pekan sibuk sebelum hari-H
        lebaran = pd.Timestamp("2025-03-31")
        jelang = 0 <= (lebaran - tgl).days <= 21
        n_trans = rng.poisson(1.9 * (2.4 if jelang else 1.0))
        promo_hari = bool(rng.random() < 0.18)

        for _ in range(n_trans):
            p = PRODUK.sample(1, random_state=int(rng.integers(1e9))).iloc[0]
            kanal = rng.choice(["toko", "online", "reseller"],
                               p=[0.50, 0.32, 0.18])
            mu = (6.0
                  * EFEK_PRODUK[p["produk"]]
                  * EFEK_KANAL[kanal]
                  * EFEK_HARI[tgl.dayofweek]
                  * (EFEK_PROMO if promo_hari else 1.0)
                  * (EFEK_LEBARAN[p["kategori"]] if jelang else 1.0))
            jumlah = int(rng.gamma(3.0, mu / 3.0)) + 1
            baris.append({
                "tanggal": tgl,
                "produk": p["produk"],
                "kategori": p["kategori"],
                "harga": p["harga"],
                "kanal": kanal,
                "promo": promo_hari,
                "jumlah": jumlah,
            })

    df = pd.DataFrame(baris)
    df["hari"] = df["tanggal"].dt.day_name()
    df["bulan"] = df["tanggal"].dt.month
    df["omzet"] = df["jumlah"] * df["harga"]
    df["borongan"] = (df["jumlah"] >= 20).astype(int)
    return df.reset_index(drop=True)
