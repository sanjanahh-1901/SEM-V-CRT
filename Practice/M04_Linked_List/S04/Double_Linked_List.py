class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None 

class Double_LL:
    def __init__(self):
        self.head = None
    def insert_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node
    def traverse(self):
        if self.head:
            return
        temp = self.head
        while temp:
            print(temp.data, end = " <-> ")
            temp = temp.next
        print("None")

dll = Double_LL()
dll.insert_begin(10)
dll.insert_begin(20)
