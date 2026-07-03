class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import defaultdict
        mydict= defaultdict(int)
        for i in nums:
            mydict[i]+=1
        
        out= sorted(mydict.items(), reverse= True, key= lambda x:x[1])
        return out[0][0]