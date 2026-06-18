class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit= 0
        leastbuyprice= 100000000
        for i in range(0, len(prices)):
            profit= prices[i]- leastbuyprice
            if profit>maxprofit:
                maxprofit= profit
            if prices[i]< leastbuyprice:
                leastbuyprice= prices[i]
        
        return maxprofit


        