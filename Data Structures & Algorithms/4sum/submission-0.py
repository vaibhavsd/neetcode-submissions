class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        totallen= len(nums)
        mlist= []
        for idx1, val1 in enumerate(nums):

            if idx1>0 and val1==nums[idx1-1]:
                continue
            
            
            for i in range(idx1+1, totallen):
                val2= nums[i]
                if i>idx1+1 and val2==nums[i-1]:
                    continue

                tarnew= -val1-val2+target
                left= i+1
                right= totallen-1
                while left<right:
                    sum= (nums[left]+nums[right])
                    if tarnew== sum:
                        mlist.append([nums[idx1], nums[i], nums[left], nums[right]])
                        left+=1
                        right-=1

                        while left<right and nums[left]==nums[left-1]:
                            left+=1
                        while left<right and nums[right]==nums[right+1]:
                            right-=1
                    elif tarnew>sum:
                        left+=1
                    else:
                        right-=1
                
        return mlist




