import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        nums = [-x for x in stones]

        heapq.heapify(nums)
        print(nums)
        while len(nums)>1:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            print(x,y) 
            if x == y:
                continue
            # elif x < y:
            #     val = y - x
            #     heapq.heappush(nums, val)
            else:
                val = x - y
                heapq.heappush(nums, val)
        if nums:
            return -nums[0]
        else:
            return 0



