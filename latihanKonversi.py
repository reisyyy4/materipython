# Latihan konversi satuan temperature
# Program konversi celcius ke satuan lain
print("\nProgram Konversi Temperature\n")

celsius = float(input("Masukkan suhu dalam celcius: "))
print("suhu adalah ", celsius, "Celsius")

# Reamur
reamur = (4/5) * celsius
print("suhu adalah ", reamur, "Reamur")

# Fahrenheit
fahrenheit = ((9/5) * celsius) + 32
print("suhu adalah ", fahrenheit, "Fahrenheit")

# Kelvin
kelvin = celsius + 273
print("suhu adalah ", kelvin, "Kelvin")

# Latihan Konversi Fahreinheit -> Kelvin dan Kelvin -> Fahreinheit

# 1. Fahreinheit -> Kelvin
print("\nProgram Konversi Temperature\n")

fahrenheit = float(input("Masukkan suhu dalam fahrenheit: "))
kelvin = ((5/9) * (fahrenheit - 32)) + 273
print("suhu adalah ", kelvin, "Kelvin")

# 2. Kelvin -> Fahrenheit
print("\nProgram Konversi Temperature\n")

kelvin = float(input("Masukkan suhu dalam fahrenheit: "))
fahrenheit = ((9/5) * (kelvin - 273)) + 32
print("suhu adalah ", fahrenheit, "fahrenheit")