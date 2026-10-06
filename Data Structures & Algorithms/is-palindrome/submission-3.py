class Solution:
    def isPalindrome(self, s: str) -> bool:
        def is_valid(c):
            return (c >='0' and c <= '9') or (c>= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z')

        l = 0
        r = len(s) - 1
        while l< r:
            
            while l < r and not is_valid(s[l]):
                l+=1
            while l < r and not is_valid(s[r]):
                r-=1

            if s[l].lower() != s[r].lower():
                return False
            
            l+=1
            while l < r and not is_valid(s[l]):
                l+=1
            r-=1
            while l < r and not is_valid(s[r]):
                r-=1

        return True