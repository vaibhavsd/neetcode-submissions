class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i= 0
        while True:
            k= len(nums)
            if i>=k:
                break
            if nums[i]== val:
                nums.pop(i)
            else:
                i+=1
        return i+1