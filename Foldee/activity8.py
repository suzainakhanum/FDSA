class CircularNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.tail = None

    def insert_at_end(self, data):
        new_node = CircularNode(data)
        if self.tail is None:
            self.tail = new_node
            self.tail.next = self.tail  # Circular link to itself
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node

    def delete_node(self, data):
        if self.tail is None:
            print("List is empty.")
            return

        current = self.tail.next
        prev = self.tail

        while True:
            if current.data == data:
                if current == self.tail and current.next == self.tail:
                    # Only one node in the list
                    self.tail = None
                else:
                    prev.next = current.next
                    if current == self.tail:
                        self.tail = prev
                print(f"Deleted node with data: {data}")
                return
            prev = current
            current = current.next
            if current == self.tail.next:
                break

        print(f"Node with data {data} not found.")

    def display(self):
        if self.tail is None:
            print("List is empty.")
            return
        current = self.tail.next
        print("Circular Linked List:", end=" ")
        while True:
            print(current.data, end=" ")
            current = current.next
            if current == self.tail.next:
                break
        print()

# Example usage
cll = CircularLinkedList()
cll.insert_at_end(10)
cll.insert_at_end(20)
cll.insert_at_end(30)
cll.display()

cll.delete_node(20)
cll.display()

cll.delete_node(100)  # Not in list
