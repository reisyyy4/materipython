'''
    Type Casting and Type Conversion

    Types of Casting
    1. Implicit = convert automatically
    2. Explicit = by using function

    int() = will convert to int data from any data type
    float() = will convert to float data from any data type
    str() = will convert to string data from any data type
    bool() = will conveert to boolean data from any data type

    input() = taking inputs from user,  entering values dynamically keyboard
    Example:
    x = float(input("Please Enter Number 1: "))
    y = float(input("Please Enter Number 2: "))
    sum = x + y
    print(sum)

    range() = will generate numbers, syntax --> range(start, stop, step)
    Example:
    for x in range(1, 21, 1):
        print(x, end=" ")
'''
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

# Input 
x = float(input("Please Enter Number 1: "))
y = float(input("Please Enter Number 2: "))
sum = x + y
print(sum)

# Range
for x in range(1, 21, 2):
    print(x, end=" ")