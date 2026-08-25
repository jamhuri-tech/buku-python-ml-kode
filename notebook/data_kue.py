"""Data bersama untuk Bab 10 dan Bab 11."""
import pandas as pd, numpy as np

def muat():
    produk = pd.DataFrame({
        "id_produk": ["P1","P2","P3","P4","P5","P6"],
        "nama": ["Nastar","Kastengel","Putri Salju","Brownies",
                 "Bolu Pandan","Lapis Legit"],
        "kategori": ["kering","kering","kering","basah","basah","basah"],
        "harga": [85000, 95000, 78000, 45000, 40000, 120000],
    })
    rng = np.random.default_rng(11)
    tgl = pd.to_datetime([
     "2025-11-03","2025-11-08","2025-11-15","2025-11-22","2025-11-29",
     "2025-12-05","2025-12-11","2025-12-18","2025-12-20","2025-12-24",
     "2026-01-04","2026-01-09","2026-01-17","2026-01-25","2026-01-31"])
    ids = ["P1","P4","P2","P5","P1","P3","P2","P4","P3","P1",
           "P1","P2","P4","P5","P3","P1","P2","P4","P1","P3",
           "P5","P2","P3","P1","P4","P2","P1","P5","P3","P9"]
    trans = pd.DataFrame({"tanggal": np.repeat(tgl,2), "id_produk": ids})
    trans["jumlah"] = rng.integers(2,25,len(trans)).astype("float64")
    trans.loc[[4,17],"jumlah"] = np.nan
    return produk, trans

def gabung():
    produk, trans = muat()
    t = trans.dropna(subset=["jumlah"]).copy()
    t["jumlah"] = t["jumlah"].astype("int64")
    g = t.merge(produk, on="id_produk", how="inner")
    g["omzet"] = g["jumlah"] * g["harga"]
    return produk, trans, g


def setahun():
    """Data satu tahun dengan cacat yang disengaja, untuk Bab 11."""
    rng = np.random.default_rng(2026)
    produk, _ = muat()
    produk = produk.set_index("id_produk")

    # intensitas musiman: kue kering memuncak saat Lebaran (Maret 2025)
    # dan akhir tahun; kue basah relatif rata.
    bulan = pd.period_range("2025-02", "2026-01", freq="M")
    int_kering = [18, 55, 30, 16, 15, 14, 16, 15, 20, 34, 22, 15]
    int_basah  = [20, 26, 22, 19, 20, 21, 19, 22, 20, 24, 21, 20]

    baris = []
    for b, ik, ib in zip(bulan, int_kering, int_basah):
        for kat, n in [("kering", ik), ("basah", ib)]:
            kand = produk.index[produk["kategori"] == kat]
            for _ in range(n):
                pid = rng.choice(kand)
                hari = rng.integers(1, b.days_in_month + 1)
                jml = int(rng.gamma(2.2, 4.0) + 1)
                baris.append({
                    "tanggal": pd.Timestamp(b.year, b.month, hari),
                    "id_produk": pid,
                    "jumlah": jml,
                    "channel": rng.choice(["toko", "online", "reseller"],
                                          p=[0.5, 0.32, 0.18]),
                })
    df = pd.DataFrame(baris)

    # pesanan borongan sesekali (pencilan yang sah)
    for i in rng.choice(len(df), 6, replace=False):
        df.loc[i, "jumlah"] = int(rng.integers(120, 260))

    # --- cacat yang disengaja ---
    dup = df.sample(4, random_state=1)
    df = pd.concat([df, dup], ignore_index=True)          # duplikat
    df.loc[rng.choice(len(df), 9, replace=False), "jumlah"] = np.nan
    df.loc[rng.choice(len(df), 3, replace=False), "jumlah"] = -5
    df.loc[rng.choice(len(df), 2, replace=False), "channel"] = "Toko"

    df = df.sample(frac=1, random_state=7).reset_index(drop=True)
    return produk.reset_index(), df
