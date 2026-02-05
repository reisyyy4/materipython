'''
    Comprehension in Python
    Comprehensions offer an easy and compact way of creating list, set, and dictionaries 
    A comprehension works by looping or iterating over items and assigning them to a container like list, set or dictionary
    This container cannot be a tuple as tuple being immutable is unable to receive assignments

    List Comprehension
    List comprehension consists of brackets containing an expression followed by a for clause, and zero or more for or if clauses
    So general form of a list comprehension is 
    list = [expression for var in sequence [optional for and/or if]]
    Syntax
    newlist = [expression for item in iterable if condition == True] --> (if condition == True) Optional

    Dictionary Comprehension
    Just like list comprehension is a way to create lists from other lists, dictionary comprehension is a way to create a python dictionary from another dictionary
    of from any other iterable. We can create new dictionaries with the same elements from the original dictionary based on conditional statements or we can transform
    the item in the dictionary according to our need. We can either modify the keys or the values or both key and value of items in the dictionary while creating a
    new dictionary using dictionary comprehension
    Syntax
    myDict = {key:value for var in iterable}
    myDict = {key:value for var in list_name}
    myDict = {key:value for var in tuple_name}
    myDict = {key:value for (key, value) in dict_name.items()}

'''

# List
mylist = []
for x in range(1, 11):
    mylist.append(x**3)
print(mylist)

# List Comprehension
newlist = [x ** 3 for x in range(1, 11)]
print(newlist)

newlist = [x ** 3 for x in range(1, 11) if x % 2 != 0]
print(newlist)

# Dictionary comprehensions
mylist = [1,2,3,4,5,6]
myDict = {x : x**3 for x in mylist}
print(myDict)

myDict = {1:1, 2:2, 3:3, 4:4, 5:5}
mynewdict = { x : x**3 for (x,x) in myDict.items()}
print(mynewdict)