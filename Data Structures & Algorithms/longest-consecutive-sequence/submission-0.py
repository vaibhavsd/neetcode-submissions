class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset= set(nums)
        maxsum= 0
        for i in myset:
            if not i-1 in myset:
                sum= 1
                while True:
                    if i+1 in myset:
                        sum+=1
                        i+=1
                    else:
                        if sum>maxsum:
                            maxsum= sum
                        break
        return maxsum        
                    