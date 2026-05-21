class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        len_ = len(nums)
        nums.sort()
        res = []
        for i in range(len_):
            ## For each number run two pointer
            if i>0 and nums[i]==nums[i-1]:
                continue
            l = i+1
            r = len_-1
            while l<r:
                if nums[l]+nums[r]+nums[i]==0:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1 ## To skip duplicate left value
                elif nums[l]+nums[r]+nums[i]>0:
                    r-=1
                else:
                    l+=1
        return res