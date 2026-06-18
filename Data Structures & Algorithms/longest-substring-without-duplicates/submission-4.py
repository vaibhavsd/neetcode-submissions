class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxlen= 0
        fastptr= 0
        slowptr= 0
        mset=set()
        mlen=0
        while fastptr<len(s):
            if s[fastptr] not in mset:
                mset.add(s[fastptr])
            
                mlen+=1
                fastptr+=1
            else:
                if mlen>maxlen:
                    maxlen= mlen
                while (s[slowptr]!= s[fastptr] and slowptr<fastptr):
                    mset.remove(s[slowptr])
                    slowptr+=1
                    mlen-=1
                mset.remove(s[slowptr])   
                slowptr+=1
                mlen-=1
        if mlen>maxlen:
            maxlen= mlen
        return maxlen
