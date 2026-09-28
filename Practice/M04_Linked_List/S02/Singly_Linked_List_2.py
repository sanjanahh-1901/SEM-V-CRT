'''


Algorithm:
1. Create nodes
2. 
3. Connections between the nodes
4. Traverse each node 


'''
class Node:
    def __init__(self, data):
        self.next = None
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4

def traverse():
    curr = node1
    while curr:
        print(curr.data, end = " -> ")
        curr = curr.next

traverse()












class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def insert_begin(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node
def traverse(head):
    curr = head
    while curr:
        print(curr.data, end = " -> ")
        curr = curr.next
    print("None")
head = None
head = insert_begin(head, 10)
head = insert_begin(head, 20)
head = insert_begin(head, 30)
traverse(head)









def deletion_end(head):
    if head is None or head.next is None:
        print("Error")
        return None
    curr = head
    while curr.next.next:
        curr = curr.next
    del_node = curr.next
    curr.next = None
    del del_node

def insert_at_pos(node, data):
    if node is None:
        print("Error")
        return None
    new_node = Node(data)















head = None
head = insert_begin(head, 10)
head = insert_begin(head, 20)
head = insert_begin(head, 30)
print("Insertion at beginning:")
traverse(head)
print()

print("Insertion at the End:")
insert_end(head, 100)
traverse(head)
print()





print("Insertion after the Node: ")
insert_after(head, 1000)
traverse(head)
print()

print("Deletion at the beginning: ")
head = deletion_begin(head)
traverse(head)
print()

print("Deletion at the end: ")
head = deletion_end(head)
traverse(head)
print()
print("Deletion after the Node: ")
deletion_end(head)
traverse(head)
