class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        totalprofit= 0

        for i in range(len(prices)):
            if i==0:
                minbuyprice= prices[i]
                continue
            
            estprofit= prices[i]- minbuyprice
            if estprofit>0:
                totalprofit+=estprofit
                minbuyprice= prices[i]
            
            if prices[i]<minbuyprice:
                minbuyprice= prices[i]
        return totalprofit


        