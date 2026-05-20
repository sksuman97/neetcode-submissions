class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_ = {} ## target-n:index
        for i in range(len(nums)):
            if nums[i] in dict_:
                return [dict_[nums[i]], i]
            dict_[target-nums[i]] = i

        