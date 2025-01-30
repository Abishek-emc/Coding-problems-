"""Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
Example 1:
Input: nums = [2,2,1]
Output: 1
Example 2:
Input: nums = [4,1,2,1,2]
Output: 4"""
from collections import Counter
nums = [4,1,2,1,2]
nums = dict(Counter(nums))
for i in nums.keys():
    if nums[i] == 1:
        print(i)
    