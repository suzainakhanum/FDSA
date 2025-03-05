class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None 
        
class LinkedList: 
    def __init__(self): 
        self.head = None 

    def insert_at_beginning(self, data): 
        new_node = Node(data) 
        new_node.next = self.head 
        self.head = new_node 

    def insert_at_end(self, data): 
        new_node = Node(data) 
        if not self.head: 
            self.head = new_node 
            return 
        last = self.head 
        while last.next: 
            last = last.next 
        last.next = new_node  

    def delete_node(self, data):
        current = self.head

        if current and current.data == data:
            self.head = current.next  # Move head to the next node
            current = None
            return
        prev = None 
        while current and current.data != data: 
            prev = current 
            current = current.next 
        if current is None: 
            return

        prev.next = current.next 
        current = None 

    def traverse(self): 
        current = self.head 
        while current: 
            print(current.data, end=" -> " if current.next else "") 
            current = current.next 
        print()  # Ensure to print a newline at the end

# Example usage:
linked_list = LinkedList() 

# Insert elements at the beginning
linked_list.insert_at_beginning(10)  # Insert 10 at the beginning
linked_list.insert_at_beginning(20)  # Insert 20 at the beginning
linked_list.insert_at_beginning(30)  # Insert 30 at the beginning

print("Linked list after inserting 30, 20, 10 at the beginning:")
linked_list.traverse()

# Optional: Insert elements at the end for demonstration
linked_list.insert_at_end(40)  # Insert 40 at the end
print("\nLinked list after inserting 40 at the end:")
linked_list.traverse()

# Optional: Delete a node for demonstration
linked_list.delete_node(20)  # Delete node with data 20
print("\nLinked list after deleting node with data 20:")
linked_list.traverse()

# Traverse the final list
print("\nTraversing the linked list:")
linked_list.traverse()
