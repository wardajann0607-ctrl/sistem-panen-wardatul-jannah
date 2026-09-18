# Modul yang dikerjakan oleh Anggota A (Wardatul Jannah)
def hitung_total_panen(berat_kg, harga_per_kg):
    return berat_kg * harga_per_kg

if __name__ == "__main__":
    total = hitung_total_panen(100, 15000)
    print(f"Total Hasil Panen: Rp{total}")
