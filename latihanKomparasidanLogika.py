# Latihan Komparasi dan Logika

# Membuat gabungan area rentang dari angka

# 1. +++++3-------------10+++++

inputUser = float(input("Masukkan angka yang bernilai kurang dari 3 atau lebih dari 10: "))

# +++++3------------- (Memeriksa angka kurang dari 3)
isKurangDari = inputUser < 3
print(isKurangDari)
print("Kurang dari 3: ", isKurangDari)

# ------------10+++++ (Memeriksa angka lebih dari 10)
isLebihDari = inputUser > 10
print("Lebih dari 10: ", isLebihDari)

# +++++3-------------10+++++
isHasil = isKurangDari or isLebihDari
print("Angka yang anda masukkan: ", isHasil)

# 2. -----3+++++++10-----

inputUser = float(input("Masukkan angka yang bernilai lebih dari 3 dan kurang dari 10: "))

# -----3++++ (Memeriksa angka lebih dari 3)
isLebihDari = inputUser > 3 
print("Lebih dari 3: ", isLebihDari)

# +++10----- (Memeriksa angka kurang dari 10)
isKurangDari = inputUser < 10
print("Kurang dari 10: ", isKurangDari)

isHasil = isLebihDari and isKurangDari
print("Angka yang anda masukkan: ", isHasil)

# 3. -----0+++++5-----8+++++11-----

inputUser = float(input("Masukkan angka yang bernilai lebih dari 0 dan kurang dari 5: "))
inputUser1 = float(input("Masukkan angka yang bernilai lebih dari 8 dan kurang dari 11: "))

isDaerah1 = 0 < inputUser < 5
print("Daerah 1: ", isDaerah1)
isDaerah2 = 8 < inputUser1 < 11 
print("Daerah 2: ", isDaerah2)
isHasil = isDaerah1 and isDaerah2
print("Angka yang anda masukkan: ", isHasil)

# 4. +++++0-----5+++++8-----11+++++
inputUser = float(input("Masukkan angka yang bernilai kurang dari 0: "))
inputUser1 = float(input("Masukkan angka yang bernilai lebih dari 5 dan kurang dari 8: "))
inputUser2 = float(input("Masukkan angka yang bernilai lebih dari 11: "))

isDaerah1 = 0 > inputUser 
print("Daerah 1: ", isDaerah1)
isDaerah2 = 5 < inputUser1 < 8 
print("Daerah 2: ", isDaerah2)
isDaerah3 =  inputUser2 > 11
print("Daerah 3: ", isDaerah3)
isHasil = isDaerah1 and isDaerah2 and isDaerah3
print("Angka yang anda masukkan: ", isHasil)