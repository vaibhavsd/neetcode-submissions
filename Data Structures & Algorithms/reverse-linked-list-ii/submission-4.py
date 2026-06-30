# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        prev= None
        curr= head
        i= 1

        if left==right:
            return head


        while curr is not None:
            if i==left:
                fut= curr.next
                frozenprev= prev
                frozencurr= curr
                prev= curr
                curr= fut
                        
                i+=1

            elif i>left and i<right:
                fut= curr.next
                curr.next= prev
                prev= curr
                curr= fut
                i+=1

            elif i==right:
                fut= curr.next
                curr.next= prev
                if frozenprev is not None:
                    frozenprev.next= curr
                prev= curr
                curr= fut
                frozencurr.next= fut     
                i+=1
                frozenhead= prev

            else: 
                prev= curr
                curr= curr.next
                
                i+=1
        
        if left> 1:
            return head
        else:
            return frozenhead
        