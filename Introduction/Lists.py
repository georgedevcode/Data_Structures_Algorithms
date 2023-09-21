# Python Lists

"""
Python Lists are ordered collections of data just like arrays in other programming languages. 
It allows different types of elements in the list.The implementation of Python List is similar to Vectors in C++ or ArrayList in JAVA. 
The costly operation is inserting or deleting the element from the beginning of the List as all the elements are needed to be shifted. 
Insertion and deletion at the end of the list can also become costly in the case where the preallocated memory becomes full.
"""

# The simplist list in Python
Lists = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(Lists)

# Python List operations

List = ["Geeks", "For", "Geeks"]
print("\nList containing multiple values: ")
print(List)

List = [["Geeks", "For"], "Geeks"]
print(List)

# Accesing a element from the list using index number
# list using index number

print("Accessing element from the list")
print(List[0])
print(List[1])