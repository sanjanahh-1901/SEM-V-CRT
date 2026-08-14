#Leetcode 59: Spiral Matrix II

#Solution
class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:        
        left, right = 0, n - 1
        top, bottom = 0, n - 1
        res = [[0] * n for _ in range(n)]
        num = 1

        while top <= bottom and left <= right:
            #left to right
            for col in range(left, right + 1):
                res[top][col] = num
                num += 1
            top += 1
            #top to bottom
            for row in range(top, bottom + 1):
                res[row][right] = num
                num += 1
            right -= 1
            #right to left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    res[bottom][col] = num
                    num += 1
                bottom -= 1
            #bottom to top
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res[row][left] = num
                    num += 1
                left += 1
        return res

if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    n = 3
    result = sol.generateMatrix(n)

    print(f"Input: n = {n}")
    print("Output:")
    for row in result:
        print(row)



    
