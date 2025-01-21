#leetcode problem no : 7
class Solution:
    def reverse(self, x: int) -> int:
        val = 1
        if x<0:    #checking whether the integer is positive 
            x = -1*x
            val = -1
        result = 0 
        while(x!=0):
            temp = x%10  #extracting the last digit
            result = result*10+temp #adding it to the result
            x = x//10
        if  result<-(2**31) or  result>=(2**31)-1:
            return 0    
        return result*val    
        