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