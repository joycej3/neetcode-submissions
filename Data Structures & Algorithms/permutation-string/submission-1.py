class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        perm = {}

        for c in s1:
            perm[c] = 1 + perm.get(c,0)

        l = 0
        for i in range(len(s2)):
            if len(s2) - i <len(s1):
                return False
            subs = {}

            if s2[i] in perm:
                j = i
                while j < i + len(s1):
                    if s2[j] not in perm:
                        i = j
                        break
                    subs[s2[j]] = 1 + subs.get(s2[j], 0)
                    j+=1
                if perm == subs:
                    return True
        return False
                


            

