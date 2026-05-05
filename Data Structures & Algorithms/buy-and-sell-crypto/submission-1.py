class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        p = 0
        profit = 0
        while i<len(prices):
            j = i+1
            while j<len(prices):
                p = prices[j] - prices[i]
                profit = max(profit,p)
                # print(p)
                # print(profit)
                j+=1
            i+=1
        return profit
