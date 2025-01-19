class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        tot = 0
        ptr = 0
        if len(s)==1:
            return d[s]
        while ptr<len(s):
            if ptr+1<len(s)and d[s[ptr]]<d[s[ptr+1]]: #if the value of the letter is less than value of it successive letter 
                tot = tot+(d[s[ptr+1]]-d[s[ptr]]) #ptr+1 - ptr
                ptr = ptr+2
            else:
                tot = tot+d[s[ptr]]
                ptr = ptr+1
        return tot