class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = {}
        res = curr = l =0
        maxf = 0

        for r in range(len(s)):
            hm[s[r]] = 1+ hm.get(s[r],0)
            maxf = max(maxf, hm[s[r]])

            while (r-l+1) - maxf > k:
                
                hm[s[l]] -= 1
                l += 1


            res = max(res, r-l+1)
        return res

            
