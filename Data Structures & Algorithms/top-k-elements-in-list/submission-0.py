class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict= dict()
        for i in nums:
            if i in mydict:
                mydict[i]+=1
            else:
                mydict[i]= 1
        
        print(mydict)
        
        sorteddict= dict(sorted(mydict.items(), key= lambda item: item[1]))
        reversedict= dict(reversed(sorteddict.items()))
        print(reversedict)

        
        mlist= list(reversedict.keys())
        print(mlist[:k])
        return mlist[:k]
        