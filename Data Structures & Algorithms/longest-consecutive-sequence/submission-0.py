class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res = 0


        for n in nums:
            if n - 1 not in numset:
                curr = 1
                while n + curr in numset:
                    curr+=1
                res = max(res,curr)
        return res
            
