class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        dict_ = {} # To store the frequency of elements
        for n in nums:
            dict_[n] = dict_.get(n, 0)+1
        ## To store top k
        heap = []
        for key,val in dict_.items():
            heapq.heappush(heap, (val,key))
            if len(heap)>k:
                heapq.heappop(heap)
        return [y for x,y in heap]
            


        