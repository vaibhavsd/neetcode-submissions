# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1ptr= l1
        l2ptr= l2
        sol= ListNode(0)
        refsol= sol
        carry= 0
        
        while l1ptr and l2ptr:
            msum= l1ptr.val + l2ptr.val + carry
            if msum>9:
                carry= 1
            else:
                carry= 0
            val= msum%10
            sol.next= ListNode(val)
            l1ptr= l1ptr.next
            l2ptr= l2ptr.next
            sol= sol.next
        while l1ptr:
            msum= l1ptr.val + carry
            if msum>9:
                carry= 1
            else:
                carry= 0
            val= msum%10
            sol.next= ListNode(val)
            l1ptr= l1ptr.next
            sol= sol.next
        while l2ptr:
            msum= l2ptr.val + carry
            if msum>9:
                carry= 1
            else:
                carry= 0
            val= msum%10
            sol.next= ListNode(val)
            l2ptr= l2ptr.next
            sol= sol.next

        if carry==1:
            sol.next= ListNode(1)
            sol= sol.next


        return refsol.next
