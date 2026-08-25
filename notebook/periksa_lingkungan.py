"""Memeriksa apakah lingkungan kerja siap untuk buku ini."""
import sys

WAJIB = {
    "numpy": "2.0", "pandas": "3.0", "matplotlib": "3.8",
    "sklearn": "1.5", "scipy": "1.11",
}

def versi_ok(ada, minimal):
    a = [int(x) for x in ada.split(".")[:2] if x.isdigit()]
    m = [int(x) for x in minimal.split(".")[:2]]
    return a >= m

print(f"Python  {sys.version.split()[0]}")
print(f"Lokasi  {sys.executable}")
dalam_venv = sys.prefix != sys.base_prefix
print(f"Lingkungan virtual aktif: {'ya' if dalam_venv else 'TIDAK'}")
print()

kurang = []
for nama, minimal in WAJIB.items():
    try:
        m = __import__(nama)
        v = getattr(m, "__version__", "?")
        tanda = "ok " if versi_ok(v, minimal) else "TUA"
        print(f"  [{tanda}] {nama:12s} {v:10s} (minimal {minimal})")
        if tanda == "TUA":
            kurang.append(nama)
    except ImportError:
        print(f"  [ -- ] {nama:12s} belum terpasang")
        kurang.append(nama)

print()
if kurang:
    print("Belum siap. Jalankan:")
    print("  python -m pip install -U " + " ".join(
        "scikit-learn" if k == "sklearn" else k for k in kurang))
else:
    print("Lingkungan siap.")
