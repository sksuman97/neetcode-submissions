class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ## Optimal
        n_set = set(nums)
        max_=0
        for n in n_set:
            ## Will run the code if the n is the start of sequence
            if n-1 not in n_set:
                streak = 1
                while n+streak in n_set:
                    streak+=1
                max_ = max(max_, streak)
        return max_
