class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        readptr= 1
        writeptr= 1
        prevwriteptr= 0
        x= len(nums)
        while readptr<x:
            if nums[prevwriteptr]==nums[readptr]:
                readptr+=1
            else:
                nums[writeptr]=nums[readptr]
                readptr+=1
                writeptr+=1
                prevwriteptr+=1
        return writeptr


        
                