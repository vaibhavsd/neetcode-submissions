class Solution:
    def mySqrt(self, x: int) -> int:
        
        start= 1
        end= x
        while True:
            mid= (start+end)//2
            if mid*mid==x:
                return mid
            elif end-start==1:
                return start

            elif mid*mid<x:
                start= mid
            else:
                end= mid

        