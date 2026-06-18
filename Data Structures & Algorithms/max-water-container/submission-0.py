class Solution:
    def container(self, p1, p2, heights):
        width= p2-p1
        length= min(heights[p1], heights[p2])
        return length*width

    def maxArea(self, heights: List[int]) -> int:
        maxwater= 0
        pointer1= 0
        pointer2= len(heights)- 1
        while pointer1<pointer2:           
            water= self.container(pointer1, pointer2, heights)
            if water>maxwater:
                maxwater= water
            if heights[pointer1]<heights[pointer2]:
                pointer1+=1
            else:
                pointer2-=1
        return maxwater
            
        



        