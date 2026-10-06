class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        for i in range(len(s)):
            l = i
            r = i
            curr = ""
            while l >=0 and r < len(s) and s[r] == s[l]:
                if l == r:
                    curr = s[l]
                else:
                    curr = s[l] + curr + s[r]
                l -= 1
                r += 1

            if len(curr) > len(res):
                res = curr

            l = i
            r = i+1
            curr = ""
            while l >=0 and r < len(s) and s[r] == s[l]:
                if r == l + 1:
                    curr = s[l] + s[l]
                else:
                    curr = s[l] + curr + s[r]
                l -= 1
                r += 1
            
            if len(curr) > len(res):
                res = curr
        return res