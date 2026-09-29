class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        perm = {}

        for c in s1:
            perm[c] = 1 + perm.get(c,0)

        i = 0
        len1 = len(s1)
        len2 = len(s2)
        while len1 + i <= len2:


            if s2[i] in perm:
                subs = {}
                j = i
                while j < i + len(s1):
                    if s2[j] not in perm:
                        i = j
                        break
                    subs[s2[j]] = 1 + subs.get(s2[j], 0)
                    j+=1
                if perm == subs:
                    return True
            i+=1
        return False
                


            

