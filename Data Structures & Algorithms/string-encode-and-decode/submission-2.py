class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res+= str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        curr = 0
        res = []

        while curr < len(s):
            end = curr
            while(s[end] != "#"):
                end+=1
            length = int(s[curr:end])

            res.append(s[end+1:end+1+length])
            curr = end+1+length
        return res


