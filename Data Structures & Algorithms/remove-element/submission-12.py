class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        if len(nums)==0:
            return 0

        if len(nums)==1:
            if val==nums[0]:
                return 0
            else:
                return 1
        last= len(nums)-1
        writeptr= 0
        count= 0
        while writeptr<=last:
            if nums[writeptr]==val:
                nums[last], nums[writeptr]= nums[writeptr], nums[last]
                last-=1
            else:
                writeptr+=1
                count+=1
        return writeptr


