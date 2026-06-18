class Solution:
    from collections import defaultdict
    def isAnagram(self, s: str, t: str) -> bool:
        mdict1= defaultdict(int)
        for i in s:
            mdict1[i]+=1
        
        mdict2= defaultdict(int)
        for j in t:
            mdict2[j]+=1
        
        return mdict1==mdict2