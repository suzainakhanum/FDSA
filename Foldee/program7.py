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

    def insert_at_end(self, data):
        new_node = DoublyNode(data)
        if self.tail is None:
            self.head = self.tail = new_node  

        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def traverse_forward(self):
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "")
            current = current.next
        print() 
# Testing the implementation
dll = DoublyLinkedList()

# Insert elements at the beginning
dll.inserting_at_beginning(10)
dll.inserting_at_beginning(20)
print("Doubly linked list after inserting 20, 10 at the beginning:")
dll.traverse_forward()

# Insert elements at the end
dll.insert_at_end(30)
dll.insert_at_end(40)
print("\nDoubly linked list after inserting 30, 40 at the end:")
dll.traverse_forward()

# Traverse the list forward
print("\nTraversing the doubly linked list forward:")
dll.traverse_forward()
