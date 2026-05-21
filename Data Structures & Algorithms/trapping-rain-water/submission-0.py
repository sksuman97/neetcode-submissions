class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l = len(height)
        for ind in range(l):
            ## Left max including index
            l_m = max(height[:ind+1])
            ## Right max including index
            r_m = max(height[ind:])
            ## area above the bar
            area = min(l_m, r_m)-height[ind]
            res+=area
        return res        