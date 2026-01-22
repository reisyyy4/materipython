'''
    Control Flow Statement in Python
    The flow control statements are divided into three categories:
    1. Conditional statements
    2. Iterative statements
    3. Transfer statements
'''

'''
    Conditional statements:
    1. if
    2. if - else
    3. if - elif - else
    4. nested if - else
    5. shorthand if
    6. match case
'''

'''
    1. if
       In control statements, The if statement is the simplest form. it takes a condition and evaluates to either
       True or False. If the condition is True, then the True block of code will be executed, and if the condition is False,
       then the block of code is skipped, and The controller moves to the next line 
       Syntax of the if statement:
       if condition:
            statement 1
            statement 2
            statement n
'''

x = int(input("Masukkan Angka ke 1: "))
y = int(input("Masukkan Angka ke 2: "))
if x < y: # --> when condition is True executed the if block and out of the block, when condition is false no executed the if block but executed out of the block 
    print("Hai") 
print("Hallo")

'''
    2. if - else 
       The if - else statement checks the codition and executes the if block of code when the condition is True 
       and if the condition is False, it will execute the else block of code
       Syntax of the if - else statement:
       if condition:
            statement 1
       else:
            statement 2 
'''

x = int(input("Masukkan Angka ke 1: "))
y = int(input("Masukkan Angka ke 2: "))
if x < y: # --> when condition is True executed the if block, when condition is false executed the else block  
    print("Hai")
else: 
    print("Hallo")

'''
    3. if - elif - else 
       When you need to check multiple conditions. You can use if - elif - else. The elif statement checks
       multiple conditions one by one and if the condition fulfills, then executes that code
       elif --> checks multiple conditions
       Syntax of the if - elif - else statement:
       if condition -1:
            statement 1
       elif condition -2:
            statement 2
       elif condition -3:
            statement 3
            ...
       else:
            statement 
'''
x = int(input("Masukkan Angka: "))
if 90 < x < 100: # --> when condition is True executed the if block, when condition is False executed the elif  
    print("Hai")
elif 80 < x < 90: # --> when condition is True executed the elif block, when condition is False executed the elif and so on until there no elif, then it will be executed else
    print("Morning")
elif 70 < x < 80:
    print("Afternoon")
else: 
    print("Hallo")

'''
    4. Nested if else
       Syntax of the nested if - else statement:
       if condition:
          if condition:
               statement 1
          else: 
               statement 1
        else: 
            statement 1
'''

# print the greatest of above three number if all are positive
# if anyof one of number is negative "numbers should not be negative"
x = 100
y = 200
z = 300

if x > 0 and y > 0 and z > 0: # --> when condition is True executed the if, when condition is False executed outer else
    if x > y and x > z: # --> when condition is True executed the if block, when condition is False executed the elif
        print("x is greater")
    elif y > x and y > z: # --> when condition is True executed the elif block, when condition is False execute the inner else
        print("y is greater")
    else:
        print("z is greater")
else: 
    print("Negative numbers are not allowed")

'''
    Iterative statements:
    1. while
    2. for

    What is loop?
    In computer programming, a loop is a sequence of instruction that is continually repeated until a certain condition is reached
'''

'''
    1. While
       The while loop statement repeatedly executes a code block while a particular condition is true.
       Syntax:
       while condition:
             statement 1
             statement 2
             ...
             statement n
'''

x = 1
while x <= 10:
    print(x, end = " ")
    x = x + 1

x = 123
sum = 0
while x != 0:
    reminder = x % 10
    sum = sum + reminder
    x = x // 10

print(sum)

x = 123
reverse = 0
while x != 0:
    reminder = x % 10
    reverse = reverse * 10 + reminder
    x = x // 10

print(reverse)