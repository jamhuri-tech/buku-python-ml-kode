# Kode pendamping buku *Python untuk Machine Learning dan Data Science*

Repositori ini menyediakan dua jenis notebook:

- **[Praktikum mahasiswa](praktikum/)** — latihan Bab 3–17 dengan sel yang
  harus dilengkapi, pengujian terbuka, dan refleksi akhir.
- **[Contoh kode buku](notebook/)** — seluruh kode contoh yang tercetak
  di buku, satu notebook per bab, dibangkitkan langsung dari naskah LaTeX.

Untuk mengerjakan praktikum, mulai dari **[panduan dan daftar notebook
praktikum](praktikum/README.md)** atau **[unduh paket mahasiswa
Bab 3–17](https://raw.githubusercontent.com/jamhuri-tech/buku-python-ml-kode/main/praktikum/praktikum-bab-03-17-v2-MAHASISWA.zip)**.
Ekstrak ZIP, lalu impor file `.ipynb` yang dipilih ke Kaggle atau Google Colab.

Buku: **Python untuk Machine Learning dan Data Science**
oleh Mohammad Jamhuri, Hisyam Fahmi, dan Muhammad Khudzaifah.
17 bab, 307 halaman.

## Menjalankan contoh kode buku secara lokal

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

## Notebook praktikum mahasiswa

Pembaruan **17 September 2026** memuat **15 notebook praktikum**. Bab 3
menggunakan versi **v3**, sedangkan Bab 4–17 menggunakan versi **v2**.

- Satu fungsi mandiri per sel; pemanggilan dan pengujiannya terpisah.
- Spasi dan baris kosong dirapikan; sel kode paling panjang 28 baris.
- Sel `[ISI KODE]` menunjukkan pekerjaan mahasiswa; pengujian dapat dibaca.
- Bagian **Refleksi akhir** membantu mahasiswa menjelaskan pemahaman dan kesulitan.

**[Lihat notebook, tautan unduh, dan pemetaan pertemuan →](praktikum/README.md)**

Notebook mahasiswa disimpan tanpa output jawaban. Kunci asisten tidak
disertakan dalam repositori atau paket mahasiswa.

## Isi notebook contoh buku

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

## Sebagian sel contoh buku memang dirancang gagal

Buku ini mengajarkan jebakan yang lazim, jadi beberapa sel **sengaja**
memunculkan galat. Contohnya `TypeError` waktu mencoba mengubah tuple,
dan `UnboundLocalError` pada contoh lingkup. Galat itu bagian dari
pelajaran, bukan kerusakan.

## Validasi notebook contoh buku

Seluruh **187 sel dijalankan ulang** sebelum repositori ini diterbitkan,
dan **ketujuh belas notebook berjalan tuntas**. Tidak ada galat tak
terduga yang tersisa.

Tiga belas sel memunculkan galat, dan **ketiga belasnya memang
disengaja**, yaitu bagian dari pelajaran seperti dijelaskan di atas.

Delapan bab memuat sel *Persiapan* di bagian atasnya. Bab-bab itu
melanjutkan contoh dari bab sebelumnya, dan di dalam buku sambungannya
dijelaskan lewat prosa sehingga listingnya sendiri tidak mengulang
penyiapan datanya. Sel Persiapan menyediakan penyiapan itu supaya tiap
notebook dapat dijalankan sendiri dari atas.

Satu catatan kejujuran untuk Bab 15. Buku tidak mencetak pembangkit
data klasifikasinya, jadi sel Persiapan di sana berisi rekonstruksi
yang sifatnya sama, yaitu dua kelas dengan kelas positif sekitar enam
persen. **Angkanya tidak akan sama persis dengan yang tercetak di
buku.** Hal ini ditandai langsung di dalam selnya.

## Lisensi

Kode dalam repositori ini berlisensi MIT, lihat `LICENSE`. Naskah dan
prosa bukunya **tidak** termasuk, dan tetap berhak cipta penuh pada
penulisnya.
