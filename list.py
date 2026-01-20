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

    How to iterate to the list
    Syntax:
    for ... in variable:
        print(...):
    How to add items to the list
    1. Append --> add item to the end of the list
       Syntax:
       variable.append(..)
    2. Insert --> insert item any position
       Syntax:
       variable.insert(index number, object)
    3. Extend --> add another list(sublist)
       Join two list
       Example:
       [1,2,3,4,5] [6,7,8,9,10] --> Join two list
       Syntax:
       variable.extend(iterable)
    How to remove the item
    1. Remove
       Syntax:
       variable.remove(value)
    2. Pop
       Syntax:
       variable.pop(index number)
    3. Clear
       Clear or remove all item, When remove all the items, it will be empty list
       Syntax:
       variable.clear()
    4. Del statement
       remove and deletes the structure of the list
       Syntax:
       del variable 
    How to modify a single item
    Syntax:
    variable[index number] = new items
    How to modify a range of item by using slicing
    Create a new variable then fill it with a new item, then use the syntax as below
    new variable = [new item]
    old variable[start index number:stop index number] = new variable 
    
    Sorting
    Sorting means arranging items in order, sorting can bedone in two ways:
    1. Ascending order --> Low number to high
    2. Descending order --> High number to low
    Syntax:
    variable.sort() --> Ascending order
    variable.sort(reverse = True) --> Descending order

    Maximum number
    Syntax:
    max(variable)
    Minimum number
    Syntax:
    min(variable)
    Total number
    Syntax:
    sum(variable)
'''

myList1 = [10, 20, 30, 40 ,50]
myList2 = [60, 70, 80, 90 ,100]
mylist3 = list([100, 'Hello', 50.50, True])
print(myList1)

# Function len
print(len(myList1))
print(myList1[len(myList1)-1])
print(myList2)

# Index Number
print(myList1[1])
print(myList1[-1])
idx = myList1.index(40, 2)
print(idx)
print(myList1[2:4])

# Iterate to the list
for item in myList1:
    print(item)

# Add item to the list:
myList1.append(60)
myList1.insert(2, 25)
print(myList1)

# Join two list
myList1.extend(myList2)
print(myList1)

# Remove item
myList1.remove(60)
print(myList1)
myList1.pop(2)
print(myList1)
#myList1.clear()
#print(myList1)

# Modify Single item
myList1[2] = 25
print(myList1)

# Modify range of items 
l1 = [100, 200, 250]
myList1[0:2] = l1 
print(myList1)

# Sorting
myList4 = [6, 2, 4, 3, 1, 5]
myList4.sort() 
print(myList4)
myList4.sort(reverse=True)
print(myList4)

# Maximum 
mx = max(myList4)
print(mx)

# Minimum
mn = min(myList4)
print(mn)

# Total
total = sum(myList4)
print(total)