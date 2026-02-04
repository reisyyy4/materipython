# Data Penjualan (Baris = Hari, Kolom = Produk)
data_penjualan = [[100, 200, 150], 
                  [120, 210, 160], 
                  [90, 190, 140],
                  [80, -70, 150],
                  [200, 250, 200]]
nama_hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"]

def analisis_penjualan(data_angka, data_label):
    print("--- Analisis Per Hari (Baris) ---")
    data_labeling = {}
    hasil_analisis = []
    jumlah_baris = len(data_angka)
    # Loop Luar: Mengakses setiap hari (Baris)
    for i in range(jumlah_baris):
        total_harian = 0
        jumlah_kolom = len(data_angka[i])
    # Loop Dalam: Mengakses setiap Produk (Kolom)
        for j in range(jumlah_kolom):
            if data_angka[i][j] > 0:
                total_harian = total_harian + data_angka[i][j]
            else:
                 print("Data Tidak Dihitung")
        hasil_analisis.append(total_harian)
    print(hasil_analisis)

    for i in range(len(data_label)):
        data_labeling[data_label[i]] = hasil_analisis[i]
    print(data_labeling)
    return data_labeling

hasil_akhir = analisis_penjualan(data_penjualan, nama_hari)
print("Hasil Analisis per Hari: ", hasil_akhir)

print("--- Analisis Per Produk (Kolom) ---")
jumlah_kolom = len(data_penjualan[0])
for i in range(jumlah_kolom):
    total_produk = 0
    jumlah_baris = len(data_penjualan)
    for j in range(jumlah_baris):
        total_produk = total_produk + data_penjualan[j][i]

    print(f"Total Penjualan Per Produk: {total_produk}")

laporan_cabang = ["Kopi", "teh", "KOPI", "Susu", "susu", "TEH", "Kopi"]

def bersihkan_dan_hitung(data_input):
    papan_tulis = {}

    for barang in data_input:
        # --- LOGIKA ANDA DI SINI ---
        barang_baru = barang.lower()
        # 1. Ubah variabel 'barang' menjadi huruf kecil semua dulu
        # Simpan di variabel baru, misal: barang_bersih
        barang_bersih = barang_baru 

        # 2. Gunakan 'barang_bersih' untuk masuk ke logika if-else
        # (Sama seperti logika tantangan pertama Anda kemarin)
        if barang_bersih in papan_tulis:
            papan_tulis[barang_bersih] += 1
        else:
            papan_tulis[barang_bersih] = 1
            
    return papan_tulis

# Eksekusi
hasil = bersihkan_dan_hitung(laporan_cabang)
print(hasil)