# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy= ListNode()
        head= dummy
        carry= 0

        while True:
            val= 0
            if carry== 0 and l1 is None and l2 is None:
                head.next= None
                break

            if carry!=0:
                val+=carry
                carry= 0
            if l1 is not None:
                val+=l1.val
                l1= l1.next
            if l2 is not None:
                val+=l2.val
                l2= l2.next
            if val>9:
                val=val%10
                carry= 1
            else:
                carry= 0

            head.next= ListNode(val)
            head= head.next
                

        return dummy.next

