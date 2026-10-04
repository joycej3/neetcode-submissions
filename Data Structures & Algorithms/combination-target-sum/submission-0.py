class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def combine(curr_sum, i):

            if curr_sum == target:
                res.append(path.copy())
                return 
            if curr_sum > target or i >= len(nums):
                return 

            path.append(nums[i])
            combine(curr_sum + nums[i], i)
            path.pop()
            combine(curr_sum, i+1)




        combine(0,0)
        return res