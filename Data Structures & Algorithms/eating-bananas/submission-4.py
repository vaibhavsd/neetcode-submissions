class Solution:
    def getTime(self, piles, k):
        import math
        total=0
        for i in piles:
            total+= math.ceil(i/k)
        return total

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l= 1
        r= max(piles)

        while l<r:
            mid= (l+r)//2

            k= self.getTime(piles, mid)
            if k>h:
                l= mid + 1 
            else:
                r= mid 
            
        return l
        