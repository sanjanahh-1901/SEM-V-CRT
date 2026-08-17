'''
#Leetcode 1351: Count Negative Numbers in a Sorted Matrix
#Solution using 2 loops
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0 
        for i in range(m):
            for j in range(n):
                if grid[i][j] < 0:
                    count += 1
        return count

#Altenative solution using 1 loop
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0 
        for row in grid:
            for num in row:
                if num < 0:
                    count += 1
        return count 

#Another solution using 1 loop
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0 
        for i in len(grid):
            for j in range(len(grid[0])):
                if grid[i][j] < 0:
                    count += 1
        return count

#Another solution 
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0 
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] < 0:
                    count += (cols - c)
                    break
        return count

grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(Solution().countNegatives(grid)) #Output: 8

#Leetcode 832: Flipping an Image
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            row.reverse()
            for i in range(len(row)):
                row[i] = 1 - row[i]
        return image
'''

#Leetcode 84: Largest Rectangle in Histogram
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            row.reverse()
            for i in range(len(row)):
                if row[i] == 0: #logic 1
                    row[i] = 1
                else:
                    row[i] = 0
        return image  
image = [[1,1,0],[1,0,1],[0,0,0]]
print(Solution().flipAndInvertImage(image))

#row[i] = 1 if row[i] == 0 else 0 #logic 2
#row[i] = 1 - row[i] #logic 3

