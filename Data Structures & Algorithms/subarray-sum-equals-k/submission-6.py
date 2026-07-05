class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        prefixsum= 0
        ans=0
        hash= defaultdict(int)
        hash[0]= 1
        for i in range(len(nums)):
            prefixsum+=nums[i]
            if prefixsum-k in hash.keys():
                ans+=hash[prefixsum-k]
                
            hash[prefixsum]+=1
            
        return ans