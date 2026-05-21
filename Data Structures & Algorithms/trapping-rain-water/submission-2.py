class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        len_ = len(height)
        for i in range(len_):
            while stack and (height[i]>height[stack[-1]]):
                m = stack.pop() ## This is the middle where water gets stored
                if stack:
                    height_ = min(height[i], height[stack[-1]])-height[m] ## height
                    width = i-stack[-1]-1
                    res+=(height_*width)
            stack.append(i)
        return res