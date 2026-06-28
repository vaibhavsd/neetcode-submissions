# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        totallen= 0
        top= head
        while top is not None:
            top= top.next
            totallen+=1
        
        top= head
        mlist= []
        while top is not None:
            mlist.append(top.val)
            top= top.next
        
        totallen2= len(mlist)
        mlist.pop(totallen2-n)

        newtop= ListNode()
        top= newtop
        for i in mlist:
            newtop.next= ListNode(i)
            newtop= newtop.next
        
        return top.next