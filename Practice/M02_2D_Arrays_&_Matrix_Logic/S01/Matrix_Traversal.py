#Leetcode 1572: Matrix Diagonal Sum
#Solution using 2 loops
from ast import List  

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        s = 0 

        for i in range(n):
            for j in range(n):
                if i == j:                 #diagonal 1
                    s += mat[i][j]
                if i + j == n - 1:         #diagonal 2 
                    s += mat[i][j]
        if n % 2 == 1:
            s -= mat[n // 2][n // 2]
        return s

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(Solution().diagonalSum(matrix))

#Optimized solution using 1 loop
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        s = 0 

        for i in range(n):
            s += mat[i][i]                 #diagonal 1
            s += mat[i][n - 1 - i]         #diagonal 2 
        if n % 2 == 1:
            s -= mat[n // 2][n // 2]
        return s

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(Solution().diagonalSum(matrix))

#Leetcode 498: Diagonal Traverse - Imp**
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        res = []
        for d in range(rows + cols - 1):
            diag = []
            r = 0 if d < cols else d - cols + 1
            c = d if d < cols else cols - 1
            while r < rows and c >= 0:
                diag.append(mat[r][c])
                r += 1
                c -= 1
            if d % 2 == 0:
                res.extend(diag[::-1])
            else:
                res.extend(diag)
        return res 

#Leetcode 1572, 1380
