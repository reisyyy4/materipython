'''
    Dictionary in Python
    Dictionary are ordered collection of unique values stored in (Key - Value) pairs. Dictionary also have same brackets like set curly brackets 
    but it will not store like list, tuple, and set. If stores the data using (Key - Value) pairs
    Unordered collections of unique values stored in (Key - Value) pairs
    Dictionary = { key : value pair }

    Example:
    myDict = { 'no' : 100, 'name' : 'Reisya', 'age' : 20 }
    Unordered : The items in dict are stored without any index value
    Unique : Keys in dictionaries should be Unique
    Mutable : We can add/modify/remove key-value after the creation

    Characteristic Dictionary
    1. Unordered
       The items in dictionaries are stored any index value, which is typically a range of number.
       They are stored as Key - Value pairs, and the keys are their index, which will not be in any sequence 
    2. Ordered
       dictionaries are ordered, which means that the item have a defined order, and that order will not change.
       A simple hash table consists of key - value pair arranged in pseudo-random order based on the calculations from Hash Function
    3. Unique 
       As mentioned above, each value has a Key; the Keys in Dictionaries should be unique. If we store any value with a Key that
       already exists, then the most recent value will replace the old value
    4. Mutable
       The dictionaries are changeable collections, which implies that we can add or remove items after creation

    Creating a dictionary
    1. Using curly brackets
       The dictionaries are created by enclosing the comma-separated Key: Value pairs inside the {} curly brackets. The colon ':' is used
       to separate the key and value in a pair
    2. Using dict() constructor
       Create a dictionary by passing the comma-separated key: value pairs inside the dict()
    3. Using sequence
       having each item as a pair (key - value)

    Empty Dictionary
    When create a dictionary without any elements inside the curly brackets then it will be an empty dictionary

    Example:
    myDict = {}

    Accessing elements of a dictionary
    There are two different ways to access the elements of a dictionary
    1. Retrieve value using the key name inside the [] square brackets
    2. Retrieve value by passing key name as a parameter to the get() method of a dictionary

    Get all keys and values
    1. keys() --> Returns the list of all keys present in the dictionary
    2. values() --> Returns the list of all values present in the dictionary
    3. items() --> Returns all the items present in the dictionary. Each item will be inside a tuple as a key - value pair

    Iterating a dictionary
    Can iterate through a dictionary using a for - loop and access the individual keys and their corresponding values.

    Example:
    myDict = { 'no' : 1, 'name' : 'Reisya', 'age' : 20 }
    for i in myDict:
        print(i)

    Find a length of a dictionary
    In order to find the number of items in a dictionary, can use the len() function. 

    Example:
    myDict = { 'no' : 1, 'name' : 'Reisya', 'age' : 20 }
    print(len(myDict))

    Adding items to the dictionary
    Can add new items to the dictionary using the two ways
    1. Using key - value assignment
       Using a simple assignment statement where value can be assigned directly to the new key
    2. Using update() Method:
       In this method, the item passed inside the update() method will be inserted into the dictionary. The item can be another dictionary
       or any iterable like a tuple of key - value pairs

    Removing items dictionary
    1. clear() --> variable.clear()
    2. pop() --> variable.pop()
'''

# Create a dictionary

# Using curly brackets
myDict = { 'no' : 1, 'name' : 'Reisya', 'age' : 20 }
print(myDict)

# Using dict() 
studDict = dict({ 'no' : 1, 'name' : 'Reisya', 'age' : 20 })
print(studDict)

# Accessing elements of a dictionary

# Access one key value --> name
print(myDict['name'])

# Access all the keys from the dictionary
print(myDict.keys())

# Access all the value from the dictionary
print(myDict.values())

# Access all the keys and value from the dictionary
print(myDict.items())

# Iterating a dictionary

# Using for loop, getting keys 
for i in myDict:
    print(i)

# Using for loop, getting values 
for i in myDict.values():
    print(i)

# Using for loop, getting key and values 
for i in myDict.items():
    print(i)

# Find a length of a dictionary
print(len(myDict))

# Adding items to the dictionary

# Adding items to the dictionary using key - value assignment
myDict['city'] = 'magelang'
print(myDict)

# Adding items to the dictionary using update() method
myDict.update({'province' : 'central java'})
print(myDict) 

# Removing items a dictionary
print(myDict.pop('city'))
print(myDict)
print(myDict.clear())
print(myDict)