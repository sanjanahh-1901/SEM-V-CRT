#Leetcode 48: Rotate Image
#Solution using two loops
from typing import List
class Solution:
    def rotate(matrix: List[List[int]]) -> None:
        n = len(matrix)
        # Transpose the matrix
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Reverse each row
        for i in range(n):
            matrix[i].reverse() 
        return matrix
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(Solution.rotate(matrix)) #Output: [[7,4,1],[8,5,2],[9,6,3]]

#Leetcode 1886: Determine Whether Matrix Can Be Obtained By Rotation
#Solution using two loops
