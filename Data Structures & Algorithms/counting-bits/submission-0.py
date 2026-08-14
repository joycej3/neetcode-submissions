class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            bits = 0
            curr = i
            while curr:
                if curr & 1:
                    bits+=1
                curr = curr>>1
            res.append(bits)
        return res

