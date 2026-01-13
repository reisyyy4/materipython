# Operasi Komparasi

'''
    Setiap hasil dari operasi komparasi adalah boolean
    Operatornya:
    1. > 
    2. <
    3. <=
    4. >=
    5. ==
    6. !=
    7. is
    8. is not
'''

# Contoh
a = 4
b = 2

# 1. Lebih besar dari >
print("--> Lebih Besar Dari (>) <--")
hasil = a > 3
print(a, ">", 3, "=", hasil)
hasil = a > 3
print(a, ">", 3, "=", hasil)
 
# 2. Kurang dari <
print("--> Kurang Dari (<) <--")
hasil = b < 3
print(b, "<", 3, "=", hasil)
hasil = b < 3
print(b, "<", 3, "=", hasil)

# 3. Lebih besar Sama Dengan >=
print("--> Lebih Besar Sama Dengan (>=) <--")
hasil = a >= 3
print(a, ">=", 3, "=", hasil)
hasil = a >= 3
print(a, ">=", 3, "=", hasil)

# 4. Kurang dari Sama Dengan <=
print("--> Kurang Dari Sama Dengan (<=) <--")
hasil = b <= 3
print(b, "<=", 3, "=", hasil)
hasil = b <= 3
print(b, "<=", 3, "=", hasil)

# 5. Sama Dengan ==
print("--> Sama Dengan (==) <--")
hasil = a == 4
print(a, "==", 4, "=", hasil)
hasil = b == 4
print(b, "==", 4, "=", hasil)

# 6. Tidak Sama Dengan !=
print("--> Tidak Sama Dengan (!=) <--")
hasil = a != 4
print(a, "==", 4, "=", hasil)
hasil = b != 4
print(b, "==", 4, "=", hasil)

# 7. 'is' sebagai komparasi objek 
x = 5 # ini adalah assignment membuat object
y = 5
print('nilai x =', x , ',id = ', hex(id(x)))
print('nilai y =', y , ',id = ', hex(id(y)))
hasil = x is y
print("x is y =", hasil)

x = 5 # ini adalah assignment membuat object
y = 6
print('nilai x =', x , ',id = ', hex(id(x)))
print('nilai y =', y , ',id = ', hex(id(y)))
hasil = x is y
print("x is y =", hasil)

# 8. 'is not' sebagai komparasi objek 
x = 5 # ini adalah assignment membuat object
y = 5
print('nilai x =', x , ',id = ', hex(id(x)))
print('nilai y =', y , ',id = ', hex(id(y)))
hasil = x is not y
print("x is not y =", hasil)

x = 5 # ini adalah assignment membuat object
y = 6
print('nilai x =', x , ',id = ', hex(id(x)))
print('nilai y =', y , ',id = ', hex(id(y)))
hasil = x is not y
print("x is not y =", hasil)