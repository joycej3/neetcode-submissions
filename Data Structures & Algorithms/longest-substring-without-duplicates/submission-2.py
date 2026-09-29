class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        mp = {}
        l = 0

        for r in range(len(s)):
            if s[r] in mp and mp [s[r]] >= l:
                l = mp[s[r]] + 1
                mp[s[r]] = r
            
            mp[s[r]] = r

            res = max(res,r-l+1)
        
        return res


