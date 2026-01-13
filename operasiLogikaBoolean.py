# Operasi Logika atau Boolean
'''
    Operasi Boolean:
    1. NOT
    2. OR
    3. AND
    4. XOR
'''

# 1. NOT
print(" --> NOT <-- ")
a = False
c = not a
print(" data a = ", a)
print(" data c = ", c)

# 2. OR --> Jika salah satu true, maka hasilnya adalah true
print(" --> OR <-- ")
a = False
b = False
c = a or b
print(a, " or ", b, " =", c)
print(" --> OR <-- ")
a = False
b = True
c = a or b
print(a, " or ", b, " =", c)
print(" --> OR <-- ")
a = True
b = False
c = a or b
print(a, " or ", b, " =", c)
print(" --> OR <-- ")
a = True
b = True
c = a or b
print(a, " or ", b, " =", c)

# 3. AND --> Jika salah satu false, maka hasilnya adalah false
print(" --> AND <-- ")
a = False
b = False
c = a and b
print(a, " and ", b, " =", c)
print(" --> AND <-- ")
a = False
b = True
c = a and b
print(a, " and ", b, " =", c)
print(" --> AND <-- ")
a = True
b = False
c = a and b
print(a, " or ", b, " =", c)
print(" --> AND <-- ")
a = True
b = True
c = a and b
print(a, " and ", b, " =", c)

# 4. XOR --> Akan True jika salah satu true, sisanya False
print(" --> XOR <-- ")
a = False
b = False
c = a ^ b   
print(a, " and ", b, " =", c)
print(" --> XOR <-- ")
a = False   
b = True
c = a ^ b   
print(a, " and ", b, " =", c)
print(" --> XOR <-- ")
a = True   
b = False
c = a ^ b
print(a, " or ", b, " =", c)
print(" --> XOR <-- ")
a = True
b = True
c = a ^ b
print(a, " and ", b, " =", c)