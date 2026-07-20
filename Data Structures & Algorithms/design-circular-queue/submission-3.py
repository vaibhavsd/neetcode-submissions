class Node:
    def __init__(self, val=None):
        self.val= val
        self.next= next

class MyCircularQueue:

    def __init__(self, k: int):
        head= Node(0)
        dummy= head
        for i in range(k):
            dummy.next= Node(None)
            dummy= dummy.next
        
        dummy.next= head.next
        self.front= head.next
        self.tail= head
        self.count= 0
        self.maxcount= k


    def enQueue(self, value: int) -> bool:
        if self.count== self.maxcount:
            return False
        self.tail= self.tail.next
        self.tail.val= value
        self.count+=1
        print(f'front- {self.front.val}, tail- {self.tail.val}')
        return True

    def deQueue(self) -> bool:
        if self.count==0:
            return False
        self.count-=1
        self.front= self.front.next
        return True

    def Front(self) -> int:
        if self.count==0:
            return -1
        return self.front.val

    def Rear(self) -> int:
        if self.count==0:
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        if self.count==0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.count== self.maxcount:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()