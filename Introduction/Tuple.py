# Python Tuples
'''
Python tuples are similar to lists but Tuples are immutable in nature i.e. once created it cannot be modified. Just like a List, 

a Tuple can also contain elements of various types.

In Python, tuples are created by placing a sequence of values separated by ‘comma’ with or without the use of parentheses for grouping of the data sequence. 

Note: To create a tuple of one element there must be a trailing comma. For example, (8,) will create a tuple containing 8 as the element.
'''

Tuple = ("Jorge", "Cerdas")

print(Tuple)

list = [1, 2, 3, 4]

Tuple = tuple(list)

print(Tuple)

#Accessing element using indexing
print(Tuple[0])

# Accessing the last element
print(Tuple[-1])