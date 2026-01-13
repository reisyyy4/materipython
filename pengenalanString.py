# Pengenalan string

'''
    String adalah kumpulan dari karakter. 
    Contoh:
    data = "okan" --> kumpulan dari karakter o, k, a, dan n
'''

# 1. Cara membuat string
'''
    1. Dengan menggunakan single quote '...'
    2. Dengan menggunakan double quote "..."
'''

# Dengan menggunakan single quote
data = 'Menggunakan single quote'
print(data)

# Dengan menggunakan double quote
data = "Menggunakan double quote"

# Jika single quote dan double quote digabung
print('"Halo, apa kabar?"')
print("'Halo, apa kabar?'")
print("Ini adalah hari jum'at")

# 2. Menggunakan tanda \

# Membuat tanda ' menjadi string
print('mari shalat jum\at')
print('g\day, isn\'t it?')

# Jika backslash
print("C:\\user\\Ucup")

# Jika tab
print("Halo\t Mo") # \t --> tab

# Jika Backspace
print("Halo \bMo") # \b --> backspacenya

# Newline
print("Baris pertama.\nbaris kedua.") # LF --> Line Feed biasanya di unix, macOS, linux
print("Baris pertama.\rbaris kedua.") # CR --> Carriage return biasanya di commodore, acorn, lisp 
print("Baris pertama.\r\nbaris kedua.") # CRLF --> Line feed carriage return biasanya di windows

# 3. String literal atau raw

# Contoh salah
print('C:\new folder')

# Menggunakan raw string
print(r'C:\\new folder')

# Multiline literal string
print("""
Nama : Reisya
Pekerjaan : AI Engineer
""")

# Jika multiline literal string dan raw digabungkan
print(r"""
Nama : Reisya
Pekerjaan : AI Engineer
Website : www.reisya.com/newID
""")

'''
    Operator String In Python:
    1. Concatenation Operator (+)
    2. Repetition Operator (*)
    3. Slicing Operator []
       Basic Slicing (Start:Stop)
                     (Start:Stop:Step)
                     [:]    --> All Item
                     [i:]   --> Dari Indeks i sampai akhir
                     [:i]   --> Dari Awal sampai j-1
                     [i:j]  --> Dari indeks i sampai j
                     [::-1] --> Membalik Urutan (Reverse)
    4. String Comparison Operator
       a. ==
       b. >
       c. >=
       d. <
       e. <=
       f. !=
       String Comparison Operator pada python digunakan untuk membandingkan dua buah teks. Hasil dari operasi ini selalu berupa
       nilai Boolean (True atau False). Python membandingkan string secara leksikografis (berdasarkan urutan abjad/kamus) menggunakan
       nilai karakter dari ASCII/Unicode

       What is ASCII?
       ASCII (American Standard Code for Information Interchange) is the most common character encoding format foe text data in computers
       and on the internet. In standard ASCII-encoded data, there area unique values for 128 alphabetic, numeric or special additional characters 
       and control codes

       Membership Operators:
       1. IN
          IN Operator : The membership operator IN returns True if the first operand is contained with second operand
       2. NOT IN
          The NOT IN python operator evaluates to true if it does not find the character in the specified String and false otherwise
        
'''

myStr1 = 'PYTHON'
myStr2 = 'PROGRAMMING'
myStr3 = 'LANGUAGE'

# 1. Concatenation Operator
myStr = myStr1 + " " + myStr2 + " " + myStr3
print(myStr)

# 2. Repetition Operator
mynewStr = myStr1 * 4
print(mynewStr)

# 3. Silicing Operator
print(myStr1[:])
print(myStr1[5:])
print(myStr1[:3])
print(myStr1[0:5])
print(myStr1[::-1])

# 4. String Comparison Operator
fruit1 = "apple"
fruit2 = "Apple"
print(fruit1 > fruit2)

# 5. IN
print("o" in fruit1)

# 6. NOT IN
print("u" not in fruit1)

'''
    String Formatting:
    What is string formatting?
    The process of inserting an object into predefined string is called string formatting. It allows you to create dynamic strings
    by combining variables and values
    
    Formatting a string:
    1. By using format specifier with % operator
       String                     --> " %s "
       Single Character           --> " %c "
       Floating Point Decimal     --> " %f "
       Floating Point Exponential --> " %e "
       Signed Integer Decimal     --> " %d " 
    2. string.format() method
       The format() method formats the specified string and insert them inside the string's placeholder.
       The placeholder is defined using curly brackets: {}. The placeholders are replaced by curly brackets.
       The format() method returns the formatted sting
    3. Formatting with f-strings

'''

name = 'Okan'
age = 45
avgScore = 97.50

# 1. Using format specifier
print("My name is %s and my age is %d and my Average Score is %f " %(name, age, avgScore))

# 2. string.format() method
print("My name is {} and my age is {} and my Average Score is {} ".format(name,age,avgScore))

# 3. Formatting with f-string
print(f"My name is {name} and my age is {age} and my Average Score is {avgScore} ")

'''
   String Methods:
   1. strip() Function:
      a) Removes leading spaces and also trailing spaces
      b) Removes leading Characters and also trailing characters
      strip() Function --> Hanya bisa di command prompt
      contoh point a:
      str = ' Hello World '
      str.strip() --> 'Hello World'
      Jadi, leading spaces adalah 1 space setelah pembuka pada single quote 
      sedangkan trailing spaces adalah 1 space sebelum penutup pada single quote
      lalu, bisa juga seperti berikut ini:
      contoh point b:
      str = 'ABCHELLOWORLDABC'
      str.strip(ABC) --> 'HELLOWORLD'
      Jadi, strip() Function bisa juga untuk menghilangkan awal dan akhir kata pada setelah pembuka pada single quote 
      dan penutup pada single quote
   2. lstrip() Function
      It strips leading space/characters only, if no arguments passed
      contoh:
      str = ' Hello World '
      str.lstrip() --> 'Hello World '
      str = 'abc Hello World'
      str.lstrip(abc) --> ' Hello World'
   3. split() Method 
      splits a given string into a list of small substrings according to a separator and stores in a List
      contoh:
      str = 'Python Programming Language'
      str.split() --> ['Python', 'Programming', 'Language']
      str = 'Python$Programming$Language'
      str.split($) --> ['Python', 'Programming', 'Language']
   4. join() Method: Combining Strings
      joins elements of a list, string, or tuple into a single string, separated by a separator
      contoh:
      str = [ 'P', 'Y', 'T', 'H', 'O', 'N' ]
      ''.join(str) --> 'PYTHON'
      '-'.join(str) --> 'P-Y-T-H-O-N'
   5. replace() Method
      replace a specified string with another string
      Syntax:
      string.replace(old, new, count)
      Parameters:
      old --> old substring you want to replace
      new --> new substring which would replace the old substring 
      count --> (Optional) the number of times you want to replace the old substring with the new substring

'''

str = 'Python$Programming$Language'
newStr = str.replace('$', ' ')
print(newStr)

'''
   Index
   The Index() method finds the first occurrence of the specified value
   The Index() method raises an exception if the value is not found
   The Index() method is almost the same as the find() method, the only difference is
   that the find() method returns -1 if the value is not found
   Syntax:
   string.index(value, start, end) 
'''

str = 'ANALYSIS'
newStr = str.index('S', 5)
print(newStr)

'''
   Find() method
   The find() method finds the first occurrence of the specified value
   The finf() method returns -1 if the value is not found
   Syntax:
   string.find(value, start, end)
'''

str = 'Python Programming'
newStr = str.find('P')
print(newStr)

'''
   rfind() Method
   The rfind() method finds the last occurrence of the specified value
   The rfind() method returns -1 if the value is not found
   Syntax:
   string.rfind(value, start, end)
'''

str = 'Python Programming'
newStr = str.rfind('P')
print(newStr)

'''
   Other important String methods in python
   upper() : The upper() method returns a string where all characters are in upper case
   lower() : returns the lowercased strings from the given string by converting each upper character to lowercase
   capitalize() : converts the first character of the string to a capital (uppercase) letter where 
   making all other characters in the string lowercase letters
   isupper() : method returns True if all the characters are in upper case, otherwise False. (alphabets)
   islower() : method returns True if all the characters are in lower case, otherwise False
   String swapcase() : converts upper case to lowercase and lower case to upper case
'''

str = 'python programming'
newStr = str.upper()
print(newStr)

str = 'python programming'
newStr = str.isupper()
print(newStr)

str = 'PYTHON PROGRAMMING'
newStr = str.lower()
print(newStr)

str = 'PYTHON PROGRAMMING'
newStr = str.islower()
print(newStr)

str = 'python programming'
newStr = str.capitalize()
print(newStr)

str = 'pYthon programming'
newStr = str.swapcase()
print(newStr)
