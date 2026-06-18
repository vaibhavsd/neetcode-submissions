class Solution:
    def isValid(self, s: str) -> bool:
        mystack= deque()
        mylist= ['(', '[', '{']
        for i in s:
            if i in mylist:
                mystack.append(i)
                print(mystack)
            elif not mystack:
                return False
            elif i== ')' and mystack[-1]=='(':
                mystack.pop()
            elif i== ']' and mystack[-1]=='[':
                mystack.pop()
            elif i== '}' and mystack[-1]=='{':
                mystack.pop()
            else:
                print(i, mystack[-1])
                return False
        if not mystack:
            return True
        else:
            return False


        