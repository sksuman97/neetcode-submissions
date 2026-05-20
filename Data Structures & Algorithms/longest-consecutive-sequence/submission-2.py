class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ## Brute Force
        # We will iterate each element
        # will check the sequence lenght starting from that element
        # Once the sequence ends will update the max
        # Time Complexity - O(n*n)
        n_set = set(nums)
        max_ = 0
        for n in nums:
            curr = n
            streak = 0
            while curr in n_set:
                curr+=1
                streak+=1
            max_ = max(max_,streak)
        return max_
            
