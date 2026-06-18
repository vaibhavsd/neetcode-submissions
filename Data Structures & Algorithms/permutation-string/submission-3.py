class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        c1= Counter(s1)

        if len(s2)<len(s1):
            return False
        trav= len(s2)- len(s1) + 1

        start= 0
        end= len(s1)-1
        c2= Counter(s2[start:end])

        for i in range(trav):
            c2[s2[end]]+=1
            if c2== c1:
                return True
            c2[s2[start]]-=1
            start+=1
            end+=1
            
        
        return False
