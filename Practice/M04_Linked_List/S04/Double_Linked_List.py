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
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end = " <-> ")
            temp = temp.next
        print("None")

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    def insert_at_position(self, position, data):
        if position < 0:
            return
        if position == 0:
            self.insert_begin(data)
            return
        new_node = Node(data)
        curr = self.head
        for _ in range(position - 1):
            if curr is None:
                return
            curr = curr.next
        if curr is None:
            return
        new_node.next = curr.next
        if curr.next:
            curr.next.prev = new_node
        curr.next = new_node
        new_node.prev = curr

    def delete_begin(self):
        if self.head is None:
            return
        del_node = self.head
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def delete_end(self):
        #List is empty
        if self.head is None:
            return
        #List is with a single node
        if self.head.next is None:
            self.head = None
            return
        #List with more than one node
        temp = self.head
        while temp.next.next:
            temp = temp.next
        #del_node is the node that needs to be removed
        del_node = temp.next 
        temp.next.prev = None
        temp.next = None
        del del_node 
    
    def count_nodes(self):
        if self.head is None:
            return 0 
        if self.head.next is None:
            return 1 
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def traverse(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

dll = Double_LL()
dll.insert_begin(10)
dll.insert_begin(20)
dll.traverse()
dll.insert_end(30)
dll.traverse()



