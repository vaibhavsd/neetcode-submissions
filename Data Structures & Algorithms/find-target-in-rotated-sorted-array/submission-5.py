class Solution:
    def findbreak(self, nums):
        for idx, val in enumerate(nums):
            if idx>0 and val<nums[idx-1]:
                return idx-1 
        return -1

    def findidx(self, start, end, nums, target):        
        while start<=end:
            mid= (start+end)//2
            if target==nums[mid]:
                return mid
            elif target>nums[mid]:
                start= mid+1
            else:
                end= mid-1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        breakidx= self.findbreak(nums)
        print(f'Break idx is {breakidx}')

        if breakidx==-1:
            out= self.findidx(0, len(nums)-1, nums, target)
            if out!=-1:
                return out
            else:
                return -1
        else:
            a= self.findidx(0, breakidx, nums, target)
            if a!=-1:
                return a
            print(f'not found between 0 and {breakidx}')
            b= self.findidx(breakidx+1, len(nums)-1, nums, target)
            if b!=-1:
                return b
            print(f'not found between {breakidx} and {len(nums)-1}')
            return -1