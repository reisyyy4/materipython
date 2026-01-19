'''
    List in Python
    Python list in an ordered sequence of items

    The Following are the properties of a list
    Mutable/Channgeable: The elements of the list can be modified. We can add or remove items to the list after it has been created
    Ordered: The items in the lists are ordered. Each item has a unique index value. The new items will be added to the end of the list
    Heterogeneus: The list can contain different kinds of elements i.e; They can contain elements of string, integer, boolean, or any type
    Duplicates: The list can contain duplicates i.e, lists can have two items with the same values. 

    Example:
    L = [20, 'Reisya', 95.75, [90, 95, 97]] --> 20 = L[0], 'Reisya' = L[1], 95.75 = L[2], [90, 95, 97] = L[3]
    Changeable = List is mutable and we can modify items
    Ordered = Maintain the order of the data insertion
    Heterogeneus = List can contain data of different types
    Constain duplicate = Allows duplicates data

    How to create a list?
    1. []
    2. list() --> constructors

    Function
    There in list:
    1. len() --> How many items in the list

    Index number:
    Index number always starts from zero ([0]) and always starts from left hand side, So even negative indexing number for list even we have negative index number
    Negative index numbers are starts from minus one ([-1]) and starts from right hand side

    Know the index number of any item, Using this index method we can find the index number of any item
    Syntax index method:
    variable.index(value, start, stop) --> start and stop optional

    Slicing:
    Slicing use for you want to access a range of items from the list
    Syntax:
    [Start Index:Stop Index: Step Index]
    When [..:..:..] --> Accessing all the items from index number zero to the last index number
         [..:5 :..] --> Accessing from index number zero to 5 because stop in 5 index
         [1 :..:..] --> Accessing from 1 index to the last index number
         [..:..:-1] --> Accesing reverse all items 
'''

myList1 = [10, 20, 30, 40 ,50]
mylist2 = list([100, 'Hello', 50.50, True])
print(myList1)
print(myList1[1])
print(myList1[-1])
print(len(myList1))
print(myList1[len(myList1)-1])
print(mylist2)
idx = myList1.index(40, 2)
print(idx)
print(myList1[2:4])