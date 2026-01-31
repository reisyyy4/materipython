# Data Penjualan (Baris = Hari, Kolom = Produk)

data_penjualan = [[100, 200, 150], 
                  [120, 210, 160], 
                  [90, 190, 140],
                  [80, 70, 150],
                  [200, 250, 200]]
nama_hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"]

print("--- Analisis Per Hari (Baris) ---")
data_labeling = {}
hasil_analisis = []
jumlah_baris = len(data_penjualan)
# Loop Luar: Mengakses setiap hari (Baris)
for i in range(jumlah_baris):
    total_harian = 0
    jumlah_kolom = len(data_penjualan[i])
    # Loop Dalam: Mengakses setiap Produk (Kolom)
    for j in range(jumlah_kolom):
        total_harian = total_harian + data_penjualan[i][j]

    hasil_analisis.append(total_harian)
print(hasil_analisis)

for i in range(len(nama_hari)):
    data_labeling[nama_hari[i]] = hasil_analisis[i]
print(data_labeling)


print("--- Analisis Per Produk (Kolom) ---")
jumlah_kolom = len(data_penjualan[0])
for i in range(jumlah_kolom):
    total_produk = 0
    jumlah_baris = len(data_penjualan)
    for j in range(jumlah_baris):
        total_produk = total_produk + data_penjualan[j][i]

    print(f"Total Penjualan Per Produk: {total_produk}")