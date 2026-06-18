class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque
        mdeque= deque()
        mset= {'{', '(', '['}
        mset2= {'}', ')', ']'}
        mdict= {'}': '{', ')':'(', ']':'['}
        for i in s:
            if not mdeque and i in mset2:
                return False
            if i in mset: 
                mdeque.append(i)
            else:
                if mdeque[-1]== mdict[i]:
                    mdeque.pop()
                else:
                    return False
        if mdeque:
            return False
        else:
            return True
