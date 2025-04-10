# Node class for each element in the stack
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Stack class using linked list
class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(f"Pushed: {data}")

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Nothing to pop.")
            return None
        popped_data = self.top.data
        self.top = self.top.next
        print(f"Popped: {popped_data}")
        return popped_data

    def peek(self):
        if self.is_empty():
            print("Stack is empty. Nothing to peek.")
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None

# Example usage
if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    print("Top element is:", s.peek())
    s.pop()
    s.pop()
    s.pop()
    s.pop()  # extra pop to test empty condition
