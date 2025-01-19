#1768. Merge Strings Alternately -leetcode 

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        r = ""
        for i in range(min(len(word1),len(word2))):
            r = r+ word1[i]+word2[i]
        if len(word1)>len(word2):
            r = r+word1[i+1:]
        else:
            r = r+word2[i+1:]
        return r