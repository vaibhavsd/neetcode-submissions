class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mdict= dict()
        for idx, val in enumerate(nums):
            newtar= target- val
            if val in mdict:
                return [mdict[val], idx]
            else:
                mdict[newtar]= idx
        
        