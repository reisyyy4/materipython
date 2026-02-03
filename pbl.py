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

barang_terjual = ["Kopi", "Teh", "Kopi", "Kopi", "Susu", "Teh", "Kopi", "Susu"]

def hitung_frekuensi(data_input):
    papan_tulis = {} # Dictionary Kosong
    
    # Loop mengecek setiap barang di keranjang
    for barang in data_input:
        
        # LOGIKA ANDA DI SINI
        if barang in papan_tulis:
            # KONDISI: Barang SUDAH ADA.
            # Apa yang harus dilakukan pada nilainya?
            # Clue: papan_tulis[barang] = papan_tulis[barang] + ...
            papan_tulis[barang] = papan_tulis[barang] + 1 
            
        else:
            # KONDISI: Barang BELUM ADA (Baru pertama kali).
            # Berapa angka awalnya?
            papan_tulis[barang] = 1
            
    return papan_tulis

# Eksekusi
hasil = hitung_frekuensi(barang_terjual)
print(hasil)