class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_ = {}
        for i in nums:
            if i not in dict_:
                dict_[i] = 1
            else:
                dict_[i] += 1
        heap = []
        for i,v in dict_.items():
            heapq.heappush(heap,(-v,i))
        lst = []
        for _ in range(k):
            freq,val = heapq.heappop(heap)
            lst.append(val)
                
        return lst
