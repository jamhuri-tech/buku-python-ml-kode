# Kode pendamping buku *Python untuk Machine Learning dan Data Science*

Notebook berisi seluruh kode contoh yang tercetak di buku, satu notebook
untuk tiap bab. Isinya dibangkitkan langsung dari naskah LaTeX bukunya,
sehingga kode di sini tidak pernah melenceng dari yang Anda baca.

Buku: **Python untuk Machine Learning dan Data Science**
oleh Mohammad Jamhuri, Hisyam Fahmi, dan Muhammad Khudzaifah.
17 bab, 307 halaman.

## Cara memakai

```bash
git clone https://github.com/jamhuri-tech/buku-python-ml-kode.git
cd buku-python-ml-kode
python3 -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
jupyter lab notebook/
```

Buka notebook di `notebook/`, lalu **jalankan selnya berurutan dari
atas**. Sebagian sel memakai peubah dari sel sebelumnya, jadi melompat
ke tengah tidak akan berhasil.

Tanpa memasang apa pun, notebook ini juga dapat dibuka langsung di
Google Colab maupun Kaggle. Ingat bahwa kedua layanan itu tidak membaca
`requirements.txt`, jadi periksa versi pustakanya lebih dahulu.

## Isi

| Notebook | Bab | Sel kode |
|---|---|---|
| `bab01.ipynb` | Menyiapkan Lingkungan Kerja | 2 |
| `bab02.ipynb` | Tipe Data, Peubah, dan Operator | 11 |
| `bab03.ipynb` | Percabangan dan Perulangan | 15 |
| `bab04.ipynb` | Fungsi, Lingkup, dan Modul | 14 |
| `bab05.ipynb` | Struktur Data Bawaan | 13 |
| `bab06.ipynb` | Berkas, Pengodean, dan Penanganan Galat | 14 |
| `bab07.ipynb` | Objek dan Kelas Secukupnya | 13 |
| `bab08.ipynb` | NumPy: Array, Broadcasting, Vektorisasi | 12 |
| `bab09.ipynb` | Matplotlib | 9 |
| `bab10.ipynb` | pandas | 14 |
| `bab11.ipynb` | Analisis Data Eksploratif | 7 |
| `bab12.ipynb` | SymPy | 19 |
| `bab13.ipynb` | Aljabar Linear dan Turunan Numerik | 8 |
| `bab14.ipynb` | Regresi Linear dan Gradient Descent | 6 |
| `bab15.ipynb` | scikit-learn | 9 |
| `bab16.ipynb` | Studi Kasus | 5 |
| `bab17.ipynb` | Praktik Baik dan Reproduktibilitas | 7 |

Berkas pendukung di `notebook/`:

| Berkas | Isi |
|---|---|
| `data_kue.py` | data penjualan untuk Bab 10 dan 11 |
| `data_kue2.py` | data diperkaya untuk Bab 16 |
| `periksa_lingkungan.py` | pemeriksa versi Python dan pustaka |
| `siapkan.py` | penyiapan data bersama antarbab |

## Sebagian sel memang dirancang gagal

Buku ini mengajarkan jebakan yang lazim, jadi beberapa sel **sengaja**
memunculkan galat. Contohnya `TypeError` waktu mencoba mengubah tuple,
dan `UnboundLocalError` pada contoh lingkup. Galat itu bagian dari
pelajaran, bukan kerusakan.

## Keadaan saat ini

Seluruh 186 sel dijalankan ulang sebelum repositori ini diterbitkan.

- **11 notebook berjalan tuntas** tanpa galat tak terduga, yaitu bab 1,
  2, 4, 5, 7, 8, 9, 11, 12, 13, dan 14.
- **6 notebook masih menyisakan 14 galat**, yaitu bab 3, 6, 10, 15, 16,
  dan 17.

Sebabnya bab-bab itu melanjutkan keadaan dari bab sebelumnya lewat
penjelasan prosa di buku, bukan lewat listing. Sebagian sudah ditangani
sel *Persiapan*, sisanya belum. Bab 6 juga membaca berkas contoh yang
dibuat pembaca sendiri saat mengikuti bukunya.

Perbaikannya sedang dikerjakan. Laporkan lewat *issue* bila Anda
menemukan yang lain.

## Lisensi

Kode dalam repositori ini berlisensi MIT, lihat `LICENSE`. Naskah dan
prosa bukunya **tidak** termasuk, dan tetap berhak cipta penuh pada
penulisnya.
