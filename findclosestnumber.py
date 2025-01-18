class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        m = nums[0]
        for i in nums:
            if abs(i)<abs(m): #comparing the magnitude of the numbers 
                m = i 
        if m<0 and abs(m) in nums: # if there is more than one number
            m = abs(m)     #greatest number is selected 
        return m      