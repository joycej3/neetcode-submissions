class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) ==2:
            return max(nums[0], nums[1])

        second_last = nums[0]
        last = max(nums[1], nums[0])
        for i in range(2, len(nums)):
            curr = max(nums[i] + second_last, last)
            second_last = last
            last = curr
        return curr
