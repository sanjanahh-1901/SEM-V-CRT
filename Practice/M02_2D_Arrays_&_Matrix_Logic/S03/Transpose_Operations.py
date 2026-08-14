#Leetcode 867: Transpose Matrix
#Solution using two loops
from numpy import matrix


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row, col = len(matrix), len(matrix[0])
        res = [[0] * row for _ in range(col)]
        for i in range(row):
            for j in range(col):
                res[j][i] = matrix[i][j]
        return res

if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = sol.transpose(matrix)

    print(f"Input: matrix = {matrix}")
    print("Output:")
    for row in result:
        print(row)

#Leetcode 566: Reshape the Matrix
#Solution using two loops
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        if row * col != r * c:
            return mat
        res = [[0] * c for _ in range(r)]
        for i in range(row):
            for j in range(col):
                idx = i * col + j
                res[idx // c][idx % c] = mat[i][j]
        return res