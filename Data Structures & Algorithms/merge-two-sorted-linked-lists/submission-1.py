# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1= list1
        head2= list2
        sol= ListNode()
        solhead= sol

        while head1 and head2:
            if head1.val<head2.val:
                solhead.next= ListNode(head1.val)
                solhead= solhead.next
                head1= head1.next
            else:
                solhead.next= ListNode(head2.val)
                solhead= solhead.next
                head2= head2.next
        while head1:
            solhead.next= ListNode(head1.val)
            solhead= solhead.next
            head1= head1.next
        while head2:
            solhead.next= ListNode(head2.val)
            solhead= solhead.next
            head2= head2.next
        return sol.next


