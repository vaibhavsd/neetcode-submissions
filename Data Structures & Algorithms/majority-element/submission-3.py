class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mid= len(nums)//2

        nums.sort()

        if nums[0]==nums[mid]:
            return nums[0]
        else:
            return nums[mid]