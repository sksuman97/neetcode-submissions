class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height)-1
        l_m, r_m = height[l], height[r]
        while l<r:
            if l_m<r_m:
                l+=1
                l_m = max(height[l], l_m)
                area = l_m-height[l]
            else:
                r-=1
                r_m = max(height[r], r_m)
                area = r_m - height[r]
            res+=area
        return res

        