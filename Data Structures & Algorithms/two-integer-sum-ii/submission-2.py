class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ## Binary Search
        len_ = len(numbers)
        for i in range(len_):
            l = i+1
            r = len_-1
            temp = target-numbers[i]
            while l<=r:
                m = (l+r)//2
                if numbers[m]==temp:
                    return [i+1, m+1]
                elif numbers[m]<temp:
                    l=m+1
                else:
                    r = m-1