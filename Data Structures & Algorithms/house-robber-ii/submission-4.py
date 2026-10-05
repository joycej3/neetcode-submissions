class Solution:
    def rob(self, nums: List[int]) -> int:
        def check_rob(n):
            if len(n) == 0:
                return 0
            if len(n) == 1:
                return n[0]
            if len(n) == 2:
                return max(n[0], n[1])
            prev1 = max(n[0], n[1])
            prev2 = n[0]

            for i in range(2,len(n)):
                curr = max(n[i] + prev2, prev1)
                prev2 = prev1
                prev1 = curr
            return prev1
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(check_rob(nums[1:]),check_rob(nums[:-1] ))
        