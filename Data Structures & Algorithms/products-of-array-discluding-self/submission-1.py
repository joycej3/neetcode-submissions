class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [0] * (len(nums))
        suf = [0] * (len(nums))
        res = nums
        if not nums:
            return []

        pref[0] = 1
        suf[-1] = 1
        for i  in range(1,len(nums)):
            pref[i] =nums[i-1] * pref[i-1]
        
        for i in range(len(nums) - 2, -1, -1):
            suf[i] = nums[i+1] * suf[i+1]
        
        for i  in range(len(nums)):
            res[i] = suf[i] * pref[i]
        return res


        

