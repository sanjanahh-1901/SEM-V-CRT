#Leetcode 876 
# Definition for singly-linked list.
from typing import Optional


class ListNode:
   def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        slow = head
        fast = head
        
        # Fast pointer moves two steps, slow pointer moves one step
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow

#Solution 2: Using length of linked list
#Leetcode Problem 876: Middle of the Linked List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        count = 0 
        temp = head 
        while temp:
            count += 1 
            temp = temp.next 
        mid_ind = count // 2
        temp = head 
        for i in range(mid_ind):
            temp = temp.next 
        return temp 

#Leetcode 141
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # If the fast pointer catches up with the slow pointer, there is a cycle
            if slow == fast:
                return True
                
        return False
    

#Leetcode 21
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        temp = ListNode()
        curr = temp
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next 

#Leetcode 206


