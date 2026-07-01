class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        mlist= []
        prevval= -9998922
        for idx, val in enumerate(nums):
            if val==prevval:
                continue

            tar= -val
            first= idx+1
            last= len(nums)-1
            while first<last:
                msum= nums[first]+nums[last]
                if msum==tar:
                    mlist.append([val,nums[first],nums[last]])
                    first+=1
                    last-=1
                    while first<last and nums[first]== nums[first-1]:
                        first+=1
                    while first<last and nums[last]== nums[last+1]:
                        last-=1    
                elif msum>tar:
                    last-=1
                else:
                    first+=1
            prevval= val
        
        return mlist
