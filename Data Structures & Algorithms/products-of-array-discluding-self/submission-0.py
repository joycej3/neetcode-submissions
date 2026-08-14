class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mult = 1
        res =[]
        zeros = 0
        for n in nums:
            if n ==0:
                zeros+=1
            else:
                mult *= n

        for n in nums:
            if zeros>1:
                res.append(0)
            elif zeros ==1:
                if n ==0:
                    res.append(mult)
                else:
                    res.append(0)
            else:
                res.append(mult//n)

        return res

