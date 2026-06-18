class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftarr= nums[:]
        rightarr=nums[:]
        outarr= nums[:]
        product= 1
        for idx, elem in enumerate(nums):
            if idx==0:
                leftarr[0]= 1
            else:
                product= product*nums[idx-1]
                leftarr[idx]= product
        print(leftarr)
        product= 1
        for idx in range(len(nums)-1, -1, -1):
            if idx== len(nums)-1:
                rightarr[idx]= 1
            else:
                product= product*nums[idx+1]
                rightarr[idx]= product
        
        for i in range(len(nums)):
            outarr[i]= leftarr[i]*rightarr[i]
        
        return outarr


