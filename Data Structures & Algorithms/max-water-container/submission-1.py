class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea= 0
        width= len(heights)-1
        

        i= 0
        j= width
        
        while i!=j:
            llen= min(heights[i], heights[j])
            area= width*llen
            if area>maxarea:
                maxarea= area
            if heights[i]> heights[j]:
                j-=1
            else:
                i+=1
            width-=1
        return maxarea


        