class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        from collections import Counter
        a= Counter(s1)
        print(a)
        winsize= len(s1)

        for left in range(len(s2)-len(s1)+1):
            b= Counter(s2[left:left+len(s1)])
            if a==b:
                return True
        return False