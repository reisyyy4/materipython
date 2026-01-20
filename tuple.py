'''
    What is Tuple?
    Tuple are ordered collections of heterogeneous data that are unchangeable. Heterogeneous means tuple can store variables of all types.
    Tuple has the following characteristics
    1. Ordered
       Tuples are part of sequence data types, which means they hold the order of the data insertion. It maintains the index
       value for each item
    2. Unchangeable
       Tuples are unchangeable, which means that we cannot add or delete items to the tuple after creation
    3. Heterogeneous
       Tuples are a sequence of data of different data types(like integer, float, list, string, etc;) and can be accessed 
       through indexing and slicing
    4. Contains Duplicates
       Tuples can contain duplicates, which means they can have items with the same value

    Example:
    T : (20, 'Reisya', 95.75, [94, 95, 96])
    Ordered : Maintain the order of the data insertion
    Unchangeable : Tuples are immutable and we can't modify items
    Heterogeneous : Tuples can contains data of types
    Contain Duplicates : Allows duplicates data

    How to creating a tuple?
    Can create a tuple using the two ways
    1. Using parenthesis (): A tuple is created by enclosing, comma-separated items inside rounded brackets
    2. Using a tuple() constructor: Create a tuple by passing the comma-separated items inside the tuple().

    Slicing:
    Slicing use for you want to access a range of items from the tuple
    Syntax:
    [Start Index:Stop Index: Step Index]
    When [..:..:..] --> Accessing all the items from index number zero to the last index number
         [..:5 :..] --> Accessing from index number zero to 5 because stop in 5 index
         [1 :..:..] --> Accessing from 1 index to the last index number
         [..:..:-1] --> Accesing reverse all items
    
    Unpacking tuple items into variables
    new varibale1, new variable2, ..., ... = variableTuples --> the number of new variables must match the items in the old variable

    Accessing items of a Tuple
    Tuple can be accessed through indexing and slicing. This section will guide you by accessing tuple using the following two ways
    1. Using indexing, can access any items from a tuple using its index 
    2. Using slicing, can access a range of items from a tuple

    Adding and changing items in a Tuple
    A list is a mutable type, which means we can add or modify values in it, but tuples are immutable, so they cannot be changed
    Also, because a tuple is immutable there are no built-in methods to add items to the tuple
    3 Steps modify items in a Tuple:
    1. Convert tuple to list
    2. Do add/modification/remove
    3. Convert list to tuple

    Conclusion:
    Tuple and list are the same data container. The similarity is that both are in order, both can be accessed using index numbers, both
    can store any data type(int, float, string, boolean). But the difference is that Tuple cannot be changed the data or delete the data in
    the Tuple then the tuple must be converted into the list first then the data is changed or deleted after that it is converted again to the tuple. 
    So the tuple is read only while the list read and write 
'''

# Create a tuple
myTuple1 = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print(myTuple1)
myFruitstuple = tuple(('apple', 'banana', 'orange', 'watermelon'))
print(myFruitstuple)
print(myFruitstuple[1:])
print(myFruitstuple[:3])
print(myFruitstuple[0:4:2])
print(myFruitstuple[::-1])

# Modify items in a Tuple
myFruitslist = list(myFruitstuple)
myFruitslist.append('manggo')
myFruitstuple = tuple(myFruitslist)
print(myFruitstuple)

# Unpacking Tuple
f1, f2, f3, f4, f5 = myFruitstuple
print(f1)
print(f2)
print(f3)
print(f4)