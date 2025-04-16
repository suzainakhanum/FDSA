class DoublyNode:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class doublylinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert_at_end(self,data):
        new_node= DoublyNode(data)
        if self.head is None:
            self.head=self.tail=new_node
            return
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head= new_node
    def delete_node(self):
        if self.head is None:
            print("dll is empty")
            return 
        if self.head.next is None:
            self.head =None
            return
        else:
            self.head=self.head.next
            self.head.prev=None

    def traverse(self):
        current= self.head
        while current:
            print(current.data,end='->')
            current= current.next
        print()

dll= doublylinkedlist()
dll.insert_at_end(12)
dll.insert_at_end(22)
dll.insert_at_end(34)
print("inserted at the beginning")
dll.traverse()

dll.delete_node()
print("deleted the first node ")
dll.traverse()
