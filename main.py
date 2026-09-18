def hitung_total_panen(berat_kg, harga_per_kg):
    return berat_kg * harga_per_kg

def hitung_diskon(total_harga, persentase_diskon):
    return total_harga * (persentase_diskon / 100)

if __name__ == "__main__":
    total = hitung_total_panen(100, 15000)
    diskon = hitung_diskon(total, 10)
    total_akhir = total - diskon
    print(f"Total awal: Rp{total}")
    print(f"Diskon: Rp{diskon}")
    print(f"Total bayar: Rp{total_akhir}")
