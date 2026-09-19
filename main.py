def hitung_total_panen(berat_kg, harga_per_kg):
    return berat_kg * harga_per_kg

if __name__ == "__main__":
    total = hitung_total_panen(100, 15000)
    # Hasil penyelesaian merge conflict
    print(f"Total Panen Versi Wardah & Nabila: Rp{total}")
