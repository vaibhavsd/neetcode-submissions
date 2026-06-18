class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftproduct= nums[:]
        rightproduct= nums[:]
        product= 1

        leftproduct[0]= 1
        for i in range(1, len(nums)):
            product*= nums[i-1]
            leftproduct[i]= product
        
        product= 1
        last= len(nums)-1
        rightproduct[last]= 1
        for i in range(last-1, -1, -1):
            product*= nums[i+1]
            rightproduct[i]= product
        
        out= nums[:]
        for i in range(len(nums)):
            out[i]= leftproduct[i]*rightproduct[i]


        return out


