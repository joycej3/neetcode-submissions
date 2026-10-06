class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        r = 0
        while i < len(s):
        
            while s[r] != "#":
                r+=1
            length = int(s[i:r])

            word = ""
            r += 1
            i = r
            while(r < i+length ):
                word+=s[r]
                r+=1

            res.append(word)
            i = r

        return res

