class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        myset= set()
        nums.sort()
        last= len(nums)-1
        for idx, val in enumerate(nums):
            target= - val
            frontp= idx+1
            lastp= last
            while lastp>frontp:
                if nums[frontp]+nums[lastp]==target:
                    myset.add((nums[idx], nums[frontp], nums[lastp]))
                    frontp+=1
                    lastp-=1
                elif nums[frontp]+nums[lastp]<target:
                    frontp+=1
                else:
                    lastp-=1
        mlist= []
        for i in myset:
            mlist.append(list(i))
        return mlist
