# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next is None:
            return

        dummy= head
        lllen= 0
        while dummy is not None:
            dummy= dummy.next
            lllen+=1
        print(f'Total length is {lllen}')
        midlen= lllen//2

        dummy= head
        for i in range(midlen-1):
            dummy= dummy.next
        
        lastnode= dummy
        dummy= dummy.next
        lastnode.next= None

        print(f'Second list starts at {dummy.val}')
        secondlist_start = dummy

        # Reverse the second list
        prev= None
        curr= dummy
        while curr is not None:
            temp= curr.next
            curr.next= prev
            prev= curr
            curr= temp
        
        rev_seclist_start= prev
        print(f'Second list rev starts at {prev.val}')
        
        list1= head
        list2= rev_seclist_start
        dummy= ListNode()
        # Merge the two lists
        while True:
            if list1 is not None and list2 is not None:
                dummy.next= list1
                list1= list1.next
                
                dummy= dummy.next
                
                dummy.next= list2
                list2= list2.next
                dummy= dummy.next
            else:
                if list1 is None:
                    dummy.next= list2
                else:
                    dummy.next= list1
                break

        dummy= head
        mlist= []
        while dummy is not None:
            mlist.append(dummy.val)
            dummy= dummy.next
        print(mlist)
            

            
        