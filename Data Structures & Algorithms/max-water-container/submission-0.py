class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l = len(heights)
        for i in range(l):
            for j in range(i, l):
                area = (j-i) * min(heights[i], heights[j])
                max_area = max(max_area, area)
        return max_area