class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s)==len(t):
            return False
        lists= list(s)
        listt= list(t)
        lists.sort()
        listt.sort()
        if not lists==listt:
            return False
        return True

        




        