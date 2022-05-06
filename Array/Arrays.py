# Implementation of all the operation in arrays

# Traversal operation in array
from array import *

values = array("I", [10, 20, 30, 40, 50, 60])
for value in values:
    print(value)

# Insertion operation
print("Inserting an element in an array..")
values.insert(1, 23)
for value in values:
    print(value)

# Delete Operation
print("Deleting an element in an array")
values.remove(40)
for value in values:
    print(value)

# Search Operation
print("Searching an element in an array")
print(values.index(40))

# Update an elements in an array
print("Updating an element: ")
values[2] = 45
for value in values:
    print(value)
