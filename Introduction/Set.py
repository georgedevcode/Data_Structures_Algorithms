# Python Set 

'''
Python set is a mutable collection of data that does not allow any duplication. 
Sets are basically used to include membership testing and eliminating duplicate entries. 
The data structure used in this is Hashing, a popular technique to perform insertion, deletion, and traversal in O(1) on average. 

If Multiple values are present at the same index position, then the value is appended to that index position, to form a Linked List. 
In, CPython Sets are implemented using a dictionary with dummy variables, where key beings the members set with greater optimizations to the time complexity.
'''

# Creating a Set 

Set = set([1, 2, "Jorge", 3, 4, "Cerdas"])

print(Set)

for i in Set:
    print(i)

# This what is going to print:
# 1
# 2
# 3
# 4
# Jorge
# Cerdas
# In Python, sets are unordered. However, when you print a set, the elements are displayed in a seemingly sorted order. 
# This is because the order of the elements in a set is determined by their hash values 1. The hash values of the elements are used to place them in a specific order, 
# which is why the order appears to be sorted 1.