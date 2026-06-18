class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mdict= dict()
        for i in nums:
            mdict[i]= False
        
        maxlen= 0
        maxnums= len(nums)
        traverser= 0
        while True:
            
            if traverser>=maxnums:
                break

            if mdict[nums[traverser]]==True:
                traverser+=1
            else:
                mlen=0
                origelem= nums[traverser]
                elem= origelem
                while True:
                    if elem in mdict:
                        mdict[elem]= True
                        mlen+=1
                        elem+=1
                    else:
                        break
                
                elem= origelem
                while True:
                    if elem-1 in mdict:
                        mdict[elem-1]= True
                        mlen+=1
                        elem-=1
                    else:
                        break
                
                maxlen= max(mlen, maxlen)
        
        return maxlen



