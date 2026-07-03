class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        zeroptr= 0
        twoptr=len(nums)-1
        writeptr= 0

        while writeptr<=twoptr:
            if nums[writeptr]==0:
                nums[writeptr], nums[zeroptr]= nums[zeroptr], nums[writeptr]
                writeptr+=1
                zeroptr+=1
            elif nums[writeptr]==1:
                writeptr+=1
            else:
                nums[writeptr], nums[twoptr]= nums[twoptr], nums[writeptr]
                twoptr-=1
                
        return nums


        