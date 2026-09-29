'''
Stack Operations:
1. is_empty(): Check if the stack is empty.
2. push(item): Add an item to the top of the stack.
3. pop(): Remove and return the top item from the stack.
4. peek(): Return the top item from the stack without removing it.
5. size(): Return the number of items in the stack.

Applications of Stack:
1. Expression Evaluation: Stacks are used to evaluate expressions in infix, postfix, and
    prefix notations.
2. Function Call Management: Stacks are used to manage function calls and recursion in programming languages.
3. Undo/Redo Functionality: Stacks are used to implement undo and redo functionality in
4. Syntax Parsing: Stacks are used in compilers and interpreters for parsing expressions and syntax.
5. Backtracking Algorithms: Stacks are used in backtracking algorithms to explore different paths and solutions.
'''
#Stack Implementation using List
class Stack:
    def __init__(self):
        self.s = []

    def push(self, val):
        self.s.append(val)

    def is_empty(self):
        return len(self.s) == 0

    def pop(self):
        if not self.is_empty():
            return self.s.pop()
                
    def size(self):
        return len(self.s)

    def peek(self):
        if not self.is_empty():
            return self.s[-1]
        return None
      
st = Stack()
print(st.is_empty())  # True
st.push(10) 
st.push(20) 
st.push(30)
print(st.is_empty())  # False
print(st.pop())  # 30
print(st.size())  # 2
print(st.peek())  # 20 


#Stack Implementation using Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack_LL: 
    def __init__(self):
        self.top = None
    def push(self, val):
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node
    def is_empty(self):
        return self.top is None
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.top.data
    def size(self):
        temp = self.top
        count = 0 
        while temp:
            count += 1 
            temp = temp.next()
        return count 

st_ll = Stack_LL()
print(st_11.is_empty())
st_ll.push(10)
st_ll.push(20)
st_ll.push(30)
print(st_ll.is_empty())
print(st_ll.pop())
print(st_ll.size())
print(st_ll.peek())


