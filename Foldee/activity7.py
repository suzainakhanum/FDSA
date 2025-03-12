class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def inserting_at_beginning(self, data):
        new_node = DoublyNode(data)
        if self.head is None:
            self.head = self.tail = new_node  
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
	
    def delete_at_beginning(self):
        if self.head is None:
            return None
        else:
            if self.head.next is None:  # If there's only one node
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
     
    def traverse_backword(self):
        if self.head is None:
            print("dll is empty")
        else:
            current = self.head
            while current.next is not None:
                current = current.next  # Traverse to the last node
            while current:
                print(current.data, end=" -> ")
                current = current.prev
            print("None")
            
# Testing the implementation
dll = DoublyLinkedList()

dll.inserting_at_beginning(10)
dll.inserting_at_beginning(20)
print("Doubly linked list after inserting 20, 10 at the beginning:")
dll.traverse_backword()

# delete at the beginning
dll.delete_at_beginning()
print("\nAfter deleting at the beginning:")
dll.traverse_backword()

# Traverse the list backward
print("\nTraversing the doubly linked list backward:")
dll.traverse_backword()

