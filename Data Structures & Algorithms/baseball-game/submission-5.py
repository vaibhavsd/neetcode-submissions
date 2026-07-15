class Solution:
    def calPoints(self, operations: List[str]) -> int:
        from collections import deque
        mystack= deque()
        for i in operations:
            
            if i == '+':
                mystack.append(mystack[-1]+mystack[-2])
                print(f'Appended {mystack[-1]+mystack[-2]}')
            elif i == 'D':
                if mystack:
                    mystack.append(2* mystack[-1])
                    print(f'Appended {mystack[-1]}')
            elif i == 'C':
                if mystack:
                    print(f'Removed {mystack[-1]}') 
                    mystack.pop()
            else:
                mystack.append(int(i))
                print(f'Appended {int(i)}')

        return sum(mystack)