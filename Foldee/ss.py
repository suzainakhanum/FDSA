class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None 

class Linked_List: 
    def __init__(self): 
        self.head = None 
        
    def insert_at_end(self, data): 
        new_node = Node(data) 
        if not self.head: 
            self.head = new_node 
            return 
        current = self.head 
        while current.next: 
            current = current.next 
        current.next = new_node

    def search_key(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Create a linked list
linked_list = Linked_List()

# Insert elements at the end
linked_list.insert_at_end(10)
linked_list.insert_at_end(20)
linked_list.insert_at_end(30)
linked_list.insert_at_end(40)

# Print the linked list
print("\nLinked list after inserting elements at the end:")
linked_list.traverse()

# Search for a key
key = 30
if linked_list.search_key(key):
    print(f"\nKey {key} found in the linked list.")
else:
    print(f"\nKey {key} not found in the linked list.")
