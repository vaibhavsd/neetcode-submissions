# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        curr= head
        idx= 1
        mlist= []
        while curr is not None:
            if idx>=left and idx<=right:
                mlist.append(curr.val)
            curr= curr.next
            idx+=1
        mlist2= mlist[::-1]
        print('Done reading')
        print(mlist)
        curr= head
        idx=1
        while curr is not None:
            if idx>=left and idx<=right:
                print(f"Adding {mlist[-1]}")
                curr.val= mlist[-1]
                mlist.pop()
            curr= curr.next
            idx+=1
        print('Done writing')
        print(mlist)
        return head