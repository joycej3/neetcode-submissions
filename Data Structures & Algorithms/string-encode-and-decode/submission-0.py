class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        start = 0
        while start < len(s):
            end = start
            while(s[end] != "#"):
                end+=1
            l = int(s[start:end])
        
            res.append(s[end+1: end+1+l])
            start = end + l + 1
        return res
            

        
