'''
#Leetcode Problem: 1480. Running Sum of 1d Array
Input: nums = [1,2,3,4]
Output: [1,3,6,10]

#Solution 
nums = [1,2,3,4]
res = [0] * (len(nums))  #O(n)
for i in range(len(nums)):
    curr_sum = 0
    for j in range(i+1):      #O(n^2)
        curr_sum += nums[j]
    res[i] = curr_sum
print(res)

#Optimal Solution
nums = [1,2,3,4]    
for i in range(1, len(nums)):
    nums[i] += nums[i-1]   #O(n)
print(nums)
'''

#Leetcode Problem: 1732. Find the Highest Altitude
'''
Input: gain = [-5,1,5,0,-7]
Output: 1       
'''
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        alt = [0] * (n + 1)  #O(n)
        for i in range(n):
            alt[i + 1] = alt[i] + gain[i]  #O(n)
        return max(alt)  #O(n)