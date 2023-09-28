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
    
    # Function to insert a new node at the beigning of the LinkedList
    def pushLinkedList(self,new_data):
        # Step 1: create a new node
        new_node = Node(new_data)
        # Step 2: make the new node as the head of the LinkedList
        new_node.next = self.head
        # Step 3: set the head to point to the new node
        self.head = new_node
        # Let's call printList() to check the new node added on the LinkedList
        self.printList()

    def insertAfter(self,prev_node, new_data):

        # Step 1: Check if given node is not None
        if prev_node is not None:
            # Find node on linked list
            
            # Step 2: Createa new node
            new_node = Node(new_data)
            # Step 3: Make next of new node as next of previous node
            new_node.next = prev_node.next
            # Step 4: Set the next of previous node to point to the new node
            prev_node.next = new_node.next
            # Step 5: Make next to prev_node as new node
            prev_node.next = new_node
            # Print the linked list of all nodes
            self.printList()
        else:   
            print("Given node is None")
            return 


if __name__ == '__main__':
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

    linked_list.pushLinkedList(4)

    linked_list.insertAfter(1, 5)
