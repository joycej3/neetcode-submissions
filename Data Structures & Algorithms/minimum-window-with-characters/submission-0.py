class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hm_t = {}
        seen = {}
        have = 0


        for c in t:
            hm_t[c] = 1 + hm_t.get(c,0)

        have = 0
        need = len(hm_t)
        l, r = 0,0
        minl, minr = 0, len(s)

        while r < len(s):
            seen[s[r]] = seen.get(s[r] , 0) + 1
            if s[r] in t and seen[s[r]] == hm_t[s[r]]:
                have+=1
            
            while have == need:
                if (r-l) < (minr -minl):
                    minr = r
                    minl = l
                
                seen[s[l]] -=1
                if s[l] in t and seen[s[l]] < hm_t[s[l]]:
                    have -=1

                l+=1
            r+=1


        if len(s) == minr:
            return ""
        return s[minl:minr+1]
