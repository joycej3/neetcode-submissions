class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        length = len(nums)

        for i in range(length):
            if i>0 and nums[i] == nums[i-1]:
                continue
            target = nums[i]
            l = i+1
            r = length-1
            
            while l < r:
                if l == i:
                    l+=1
                if r == i:
                    r-=1
                if l >= r:
                    continue
                
                if nums[l] + nums[r] + nums[i] > 0:
                    r-=1
                elif nums[l] + nums[r] + nums[i] < 0:
                    l+=1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    r-=1
                    l+=1
                    while(l < r and nums[l] == nums[l-1]):
                        l+=1
                    while(l < r and nums[r] == nums[r + 1]):
                        r-=1



        return res

            


        