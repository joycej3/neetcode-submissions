class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        perm = {}

        for c in s1:
            perm[c] = 1 + perm.get(c,0)

        i = 0
        len1 = len(s1)
        len2 = len(s2)
        subs = {}
        for i in range(len2):
            subs[s2[i]] = 1 + subs.get(s2[i], 0)

            if i +1 >= len1:
                if subs == perm:
                    return True
                subs[s2[i- len1 +1]] -= 1
                if  subs[s2[i- len1 +1]] ==0:
                    del subs[s2[i- len1 +1]]

        return False
                


            

