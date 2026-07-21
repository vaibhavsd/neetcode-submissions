class Solution:
    from collections import defaultdict
    def isAnagram(self, s: str, t: str) -> bool:
        mdict1= defaultdict(int)
        mdict2= defaultdict(int)
        for i in s:
            mdict1[i]+=1
        for i in t:
            mdict2[i]+=1
        if mdict1==mdict2:
            return True
        else:
            return False
