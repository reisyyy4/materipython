'''
    What is debugging? 
    A debugger is a program that can help you find out what is going on in a computer program or
    you can say debugs helps to analyze (inspects) the program line by line

    Why to debug?
    if there are any runtime error or bugs in your program, we have to debug

    What is breakpoint?
    A breakpoint is a point in a program where the program intentionally stops or pauses for debugging purpose

    How to debug?
    we will see practically

    Conclusion the Debugging Concepts:
    Knowing how to code is read sequentially or usually called the control flow, monitoring the change in the value
    of the data variable in each step, so that if an error occurs it can be easily known and why the error can occur
'''

x = 100
y = 200
z = 300

# if all the above number are negative, then print greatest of three number
# if any one of the above numbers are negative, "Negative Numbers are not allowed"

if x > 0 and y > 0 and z > 0:
    if x > y and x > z: 
        print("x is greater")
    elif y > x and y > z: 
        print("y is greater")
    else:
        print("z is greater")
else: 
    print("Negative numbers are not allowed")
