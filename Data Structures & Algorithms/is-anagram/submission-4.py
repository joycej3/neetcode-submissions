class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ms = {}
        mt = {}
        for c in s:
            ms[c] = ms.get(c,0) + 1
        for c in t:
            mt[c] = mt.get(c,0) + 1
        return mt == ms