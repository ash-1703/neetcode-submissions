class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        piles = [1,4,3,2] [no of bananas in each pile]
                 0 1 2 3
                h = 9 (total time given)
                k = ?
        """
        # brute force
        # speed = 1
        # while True:
        #     totalTime = 0
        #     for pile in piles:
        #         totalTime += math.ceil(pile/speed)
        #     if totalTime<=h:
        #         return speed
        #     speed += 1
        # return speed

        l = 1
        r = max(piles)
        res = max(piles)
        while l<=r:
            m = (l+r)//2
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(pile/m)
            if totalTime <= h:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        return res
