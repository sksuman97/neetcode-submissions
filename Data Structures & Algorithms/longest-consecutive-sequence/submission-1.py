class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # We will solve it using a for loop and and while loop
        if not nums:
            return 0

        n_set = set(nums)
        curr=1
        max_ = 1
        for n in n_set:
            while n+1 in n_set:
                curr+=1
                max_ = max(curr, max_)
                n+=1
            curr = 1
        return max_



