class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit= 0
        buyprice= prices[0]
        for i in range(len(prices)):
            if prices[i]- buyprice> maxprofit:
                maxprofit= prices[i]- buyprice
            if prices[i]< buyprice:
                buyprice= prices[i]
        return maxprofit
