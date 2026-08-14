#Leetcode 54: Spiral Matrix

#Solution using 4 loops - Imp*
from turtle import right
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1
        left, right = 0, cols - 1   
        res = []
        while top <= bottom and left <= right:
            for c in range(left, right + 1):    #left to right
                res.append(matrix[top][c])
            top += 1
            for r in range(top, bottom + 1):     #top to bottom
                res.append(matrix[r][right])
            right -= 1
            if top <= bottom:
                for c in range(right, left - 1, -1):    #right to left
                    res.append(matrix[bottom][c])
                bottom -= 1
            if left <= right:
                for r in range(bottom, top - 1, -1):    #bottom to top
                    res.append(matrix[r][left])
                left += 1
        return res

#Alternative Solution 
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1
        res = []

        while top <= bottom and left <= right:
            #left to right
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1
            #top to bottom
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1
            #right to left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1
            #bottom to top
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][left])
                left += 1
        return res
    