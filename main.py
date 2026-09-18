def hitung_total_panen(berat_kg, harga_per_kg):
    return berat_kg * harga_per_kg

def hitung_diskon(total_harga, persentase_diskon):
    return total_harga * (persentase_diskon / 100)

# Fitur pengerjaan Anggota B: cetak ringkasan laporan
def cetak_laporan_panen(berat, harga, diskon_persen):
    total = hitung_total_panen(berat, harga)
    diskon = hitung_diskon(total, diskon_persen)
    total_bayar = total - diskon
    print("=== LAPORAN RINGKASAN PANEN ===")
    print(f"Total Panen : Rp{total}")
    print(f"Potongan    : Rp{diskon}")
    print(f"Total Bayar : Rp{total_bayar}")

if __name__ == "__main__":
    cetak_laporan_panen(100, 15000, 10)
    
