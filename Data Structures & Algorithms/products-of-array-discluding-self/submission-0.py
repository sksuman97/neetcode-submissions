class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ## We will maintain two lists
        # one for pre and other for post the element array product
        l = len(nums)
        pre, res = [], [1]*l
        ## For pre
        temp = 1
        for n in nums:
            pre.append(temp)
            temp*=n
        ## for post prod
        temp = 1

        for idx, val in enumerate(nums):
            res[l-1-idx] = temp*pre[l-1-idx]
            temp*=nums[l-1-idx]
        return res

        
        