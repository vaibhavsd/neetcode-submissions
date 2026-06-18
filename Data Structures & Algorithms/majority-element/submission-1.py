class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxlen= int(len(nums)/2) + 1

        if maxlen==1:
            return nums[0]

        mydict= dict()
        for i in nums:
            if i in mydict:
                mydict[i]+=1

                if mydict[i]>=maxlen:
                    return i
            else:
                mydict[i]= 1