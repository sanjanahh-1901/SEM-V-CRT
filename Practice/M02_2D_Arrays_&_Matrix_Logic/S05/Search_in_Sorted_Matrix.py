#Leetcode 74: Search a 2D Matrix
'''
from typing import List
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    arr = []
    for row in matrix:
        arr += row
    n = len(arr)
    left, right = 0, n-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(searchMatrix(matrix, target)) #Output: True
'''

#Alternative solution without creating a new array
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid = (left + right) // 2
            row, col = mid // n, mid % n
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                right = mid - 1
            else:
                left = mid + 1
        return False
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(Solution().searchMatrix(matrix, target)) #Output: True

#Leetcode 378: Kth Smallest Element in a Sorted Matrix
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        left, right = matrix[0][0], matrix[m-1][n-1]
        while left < right:
            mid = (left + right) // 2
            count = 0
            for row in matrix:
                count += bisect.bisect_right(row, mid)
            if count < k:
                left = mid + 1
            else:
                right = mid
        return left


        