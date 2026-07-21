class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mset= set()
        left= 0
        right= 0
        count= 0
        maxcount= 0
        while right<len(s):
            if s[right] not in mset:
                mset.add(s[right])
                right+=1
                count+=1
            else:
                val= s[right]
                if maxcount<count:
                    maxcount= count
                while val in mset:
                    mset.remove(s[left])
                    left+=1
                    count-=1
        if count>maxcount:
            maxcount= count
        return maxcount
