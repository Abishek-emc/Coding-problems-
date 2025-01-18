class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        tot = 0
        for i in jewels:
            tot = tot+ stones.count(i)
        return tot
#To find number of stones which are jewels
a = Solution()
print(a.numJewelsInStones("z","ZZ")) 