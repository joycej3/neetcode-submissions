class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while (l < r):
            while (not s[l].isalnum() or s[l] == " ") and l<r:
                l+=1
            while (not s[r].isalnum() or s[r] == " ") and l<r:
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True