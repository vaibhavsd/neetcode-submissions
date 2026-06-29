"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        dummy= Node(0)
        newlist= dummy
        top= head
        mymap = {None: None}
        while top is not None:
            dummy.val= top.val

            mymap[top]= dummy
            top= top.next
            
            if top is not None:
                dummy.next= Node(0)
                dummy= dummy.next
            else:
                dummy.next= None
        print(mymap)
        
        top= head
        dummy= newlist
        while top is not None:
            dummy.random= mymap[top.random]
            dummy= dummy.next
            top= top.next


        return newlist
