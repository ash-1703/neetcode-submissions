class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         profit = max(profit, prices[j]-prices[i])
        # return profit
    
        # l = 0
        # r = 1
        # maxP = 0
        # while r<len(prices):
        #     if prices[l] < prices[r]:
        #         profit = prices[r] - prices[l]
        #         maxP = max(maxP, profit)
        #     else:
        #         l = r
        #     r += 1
        # return maxP

        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxP


        
