class Solution:
    def numDecodings(self, s: str) -> int:
        def is_valid(t,u):
            if t == '1' or t == '2' and u in '0123456':
                return True
            return False
        
        prev = 1
        prev2 = 0
        dp = 0
        for i in range(len(s)):
            #if coming from -1
            if s[i] > '0':
                dp = prev

            #if coming from -2
            if i > 0 and is_valid(s[i - 1], s[i]):
                dp = dp + prev2

            prev2 = prev
            prev = dp
            dp = 0
        return prev