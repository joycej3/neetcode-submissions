class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hms = {}
        hmt = {}

        for i in range(len(s)):
            hms[s[i]] = hms.get(s[i], 0) + 1
            hmt[t[i]] = hmt.get(t[i], 0) + 1
        return (hms == hmt)
        