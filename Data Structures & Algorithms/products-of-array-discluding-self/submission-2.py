class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftpro= [1]

        product=1
        for idx, val in enumerate(nums):
            if idx==0:
                continue
            product *= nums[idx-1]
            leftpro.append(product) 
        
        print(leftpro)
        nums2= nums[::-1]

        rightpro= [1]
        product=1
        for idx, val in enumerate(nums2):
            if idx==0:
                continue
            product *= nums2[idx-1]
            rightpro.append(product) 
        print(rightpro)

        rightpro2= rightpro[::-1]

        out= []
        for idx, val in enumerate(nums):
            out.append(leftpro[idx]*rightpro2[idx])
        
        return out