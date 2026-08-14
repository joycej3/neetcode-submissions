class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        ls = {}
        lt = {}

        for i in range(len(s)):
            ls[s[i]] = 1 + ls.get(s[i],0)
            lt[t[i]] = 1 + lt.get(t[i],0)
        return ls == lt
