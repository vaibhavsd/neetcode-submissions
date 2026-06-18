class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit= 0
        buyprice= prices[0]
        i=1
        maxelem= len(prices)
        while True:
            if i==maxelem:
                return maxprofit

            exp_profit= prices[i]- buyprice
            if exp_profit>maxprofit:
                maxprofit= exp_profit

            if prices[i]<buyprice:
                buyprice= prices[i]
            i+=1
