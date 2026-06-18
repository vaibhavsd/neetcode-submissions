class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x= len(nums)
        nums2= []

        for i in range(x):
            if i==0:
                nums2.append(nums[i])
            else:
                if (nums[i]== nums[i-1]):
                    continue;
                else:
                    nums2.append(nums[i])
        print(nums2)
        for i in range(len(nums2)):
            nums[i]= nums2[i]
        
        print(len(nums)- len(nums2))
        for i in range(len(nums)- len(nums2)):
            nums.pop()
        return len(nums2)
                