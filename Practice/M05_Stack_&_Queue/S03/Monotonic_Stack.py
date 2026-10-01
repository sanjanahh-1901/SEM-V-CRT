#Leetcode 496 - Next Greater Element I
from ast import List

def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    stack = []
    next_greater = {}
    for num in nums2:
        while stack and stack[-1] < num:
            next_greater[stack.pop()] = num
        stack.append(num)
    while stack:
        next_greater[stack.pop()] = -1
    return [next_greater[num] for num in nums1]

#Leetcode 901 - Online Stock Span
class StockSpanner:

    def __init__(self):
        # Stack stores tuples of (price, span)
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        
        # Pop all previous days' prices that are less than or equal to current price
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
            
        # Push current price and its accumulated span onto stack
        self.stack.append((price, span))
        
        return span