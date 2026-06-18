class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxlen= 0
        for k in range(len(s)):
            news= s[k:]
            myset= set()
            for i in news:
                if i not in myset:
                    myset.add(i)
                else:
                    break
            setlen= len(myset)
            if setlen>maxlen:
                maxlen= setlen
        

        return maxlen