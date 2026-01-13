# Casting adalah merubah dari satu tipe data ke tipe lain
# Berikut cara casting

# 1. Integer
data = 7
data_float = float(data)
data_string = str(data)
data_boolean = bool(data)
print("Data = ", data_float, type(data_float))
print("Data = ", data_string, type(data_string))
print("Data = ", data_boolean, type(data_boolean))

# 2. Float
data = 8.5
data_integer = int(data) # Jika tipe data float dirubah ke tipe data integer maka akan terjadi pembulatan ke bawah
data_string = str(data)
data_boolean = bool(data)
print("Data = ", data_integer, type(data_integer))
print("Data = ", data_string, type(data_string))
print("Data = ", data_boolean, type(data_boolean))

# 3. Boolean
data = False
data_integer = int(data)
data_string = str(data)
data_float = float(data)
print("Data = ", data_integer, type(data_integer))
print("Data = ", data_string, type(data_string))
print("Data = ", data_float, type(data_float))

# 4. String
data = "7"
data_integer = int(data)
data_boolean = bool(data)
data_float = float(data)
print("Data = ", data_integer, type(data_integer))
print("Data = ", data_boolean, type(data_boolean))
print("Data = ", data_float, type(data_float))