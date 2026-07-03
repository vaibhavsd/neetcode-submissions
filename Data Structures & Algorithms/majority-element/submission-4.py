class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        elem= nums[0]
        count= 0

        for i in nums:
            if i==elem:
                count+=1
            else:
                if count==0:
                    elem= i
                else:
                    count-=1
        return elem