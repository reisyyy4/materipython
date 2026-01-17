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
'''

myList1 = [10, 20, 30, 40 ,50]
mylist2 = list([100, 'Hello', 50.50, True])
print(myList1)
print(myList1[1])
print(len(myList1))
print(mylist2)
