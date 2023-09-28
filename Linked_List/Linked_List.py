# Python Linked List

'''
A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations.

A linked list is represented by a pointer to the first node of the linked list. The first node is called the head. If the linked list is empty, then the value of the head is NULL. Each node in a list consists of at least two parts:

Data
Pointer (Or Reference) to the next node
'''

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

if __name__ == 'main':
    # We instanciated the Linked List object
    linked_list = LinkedList()
    # Ceated the linked list head and the second and third node
    linked_list.head = Node(1)
    second = Node(2)
    third = Node(3)
    # Now, we set up the linked list head to target the next node
    linked_list.head.next = second
    # The second node targets to the third node
    second.next = third

    linked_list.printList()