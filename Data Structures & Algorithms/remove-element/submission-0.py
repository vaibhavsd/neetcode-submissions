class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        totallen= len(nums)
        target= val
        counter= 0
        i=0
        while counter < totallen:
            if nums[i]==target:
                counter+=1
                nums.pop(i)
            else:
                counter+=1
                i+=1
        print(nums)
        return len(nums)