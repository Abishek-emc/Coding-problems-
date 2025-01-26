class Solution:
    def missingNumber(self, arr):
        cur = 1
        arr.sort()#sort the array
        for i in range(len(arr)):
            if arr[i] != cur: #checking arr[i] to current value if not return cur 
                return cur
            cur = cur +1 #increment the cur  
        return cur   