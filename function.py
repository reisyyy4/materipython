'''
    Python Functions
    In python, the funtion is a block of code defined with a name. We use function whenever we need to perform the same task multiple
    times without writing the same code again. It can take arguments and returns the value
    Python has a DRY principle like other programming languages. DRY stands for Don't Repeat Yourself. Consider a scenario where we need to
    do some action/task many times. We can define that action only once using a function and call that function whenever required to do the same
    activity
    Function improves effiencey and reduces errors because of the reusability of a code. Once we create a function, we can call it anywhere and anytime
    The benefit of using a function is reusability and modularity

    Types of Functions
    Python support two types of function
        1. Built-in function
        2. User-defined function

    1. Built-in function
       The function which are come along with Python itself are called a built-in function or predefined function. Some of them are listed below
       range(), id(), type(), input(), eval() etc
    
    2. User-defined function
       Syntax for defining a Function:
       def ..... ([input parameters]):
            [ block of code ]
       We should not use print() inside any function, we must use return statement
       return the output

    Two type of variables in Function
    1. Local Variable: Declared inside the function, these variables can be accessed local
    2. Global Variable: Declared out side, can be accessed any where 
       Key word ___ global key word ___ to make local variable as global

    Types of arguments in Function
    1. Positional Arguments
       Positional arguments are arguments that are pass to function in proper positional order. That is, the 1st positional argument needs to be
       1st when the function is called. The 2nd positional argument needs to be 2nd when the function is called, etc
    2. Keyword Arguments
       A keyword arguments is an argument value, passed to function preceded by the variable name and an equals sign
    3. Default Arguments
    4. Variable-length Arguments
       In Python, sometimes, there is a situation where we need to pass multiple numbers of arguments to the function. Such types of arguments
       are called variable-length arguments. We can declare a variable-length argument with the * (asterisk) symbol
'''

# User-defined function
def factorialNumber():
    n = int(input("Please write your number: "))
    fact1 = 1

    for x in range(1, n + 1):
        fact1 = fact1 * x
    print(fact1)

factorialNumber()

def factorialNumber(n):
    fact1 = 1

    for x in range(1, n + 1):
        fact1 = fact1 * x
    print(fact1)

factorialNumber(6)

def addTwoNumbers(x, y):
    sum = x + y
    print(sum)

addTwoNumbers(10, 20)

# Use return statement
def addThreeNumber(x, y, z):
    sum = x + y + z
    return sum 

result = addThreeNumber(10, 20, 30)
print(result)

def sqrtFunction(x):
    res = x ** 0.5
    return res

result = sqrtFunction(49)
print(result)

# Two type of variable in function
global_lang = 'Python Programming Language'
def demo1():
    local_lang = 'Java Programming Language'
    print(local_lang)
    print(global_lang)

demo1()
print(global_lang)
# print(local_lang) --> Tidak bisa karena local hanya bisa diakses di dalam function
# jika global_lang --> bisa diakses di dalam function ataupun di luar function

# Global key word to make local variable as global
def demo2():
    global l_var
    l_var = 'Java Programming Language'
    print(l_var)
    print(global_lang)

demo2()
print(l_var)

# Positional arguments
def addNumbers(x, y):
    print(x - y)

print(addNumbers(100, 200)) # Output -100
print(addNumbers(200, 100)) # Output 100

# Keyword arguments
def message(name, surname):
    print("Hello", name, surname)

message(name = "Reisya", surname = "Okan")
message(surname = "Reisya", name = "Okan")