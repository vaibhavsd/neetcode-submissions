class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start= 0
        end= len(nums)-1
        while start<end:
            mid= (start+end)//2
            if nums[mid]<nums[mid+1]:
                start=mid+1
            elif nums[mid]>nums[mid+1]:
                end= mid
        return start
