"""Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums."""
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        cur = 1
        prev = nums[0]
        while(cur<len(nums)):
            if nums[cur]== prev:
                nums.pop(cur)
            else:
                prev = nums[cur] 
                cur = cur+1