# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowp= head
        fastp= head
        while slowp is not None and fastp is not None:
            slowp= slowp.next
            if fastp.next is None:
                return False
            elif fastp.next.next is None:
                return False
            else:
                fastp= fastp.next.next

            if slowp==fastp:
                return True
        return False 
            