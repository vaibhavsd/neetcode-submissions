class Solution:
    def mysearch (self, nums, target, start, fin):
        mid= (start+fin)//2

        if start>fin or start<0:
            return -1
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            return self.mysearch(nums, target, start, mid-1)
        else:
            return self.mysearch(nums, target, mid+1, fin)



    def search(self, nums: List[int], target: int) -> int:
        return self.mysearch(nums, target, 0, len(nums)-1) 