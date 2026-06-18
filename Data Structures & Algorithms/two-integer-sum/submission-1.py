class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mydict= dict()
        for i in range(0, len(nums)):
            if target-nums[i] in mydict.keys():
                if i>mydict[target-nums[i]]:
                    return [mydict[target-nums[i]], i]
                else:
                    return [i, mydict[target-nums[i]]]
                    
            else:
                mydict[nums[i]]= i

