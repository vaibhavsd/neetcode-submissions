class ListNode:
    def __init__(self, key):
        self.key= key
        self.next= None

class MyHashSet:

    def __init__(self):
        self.maxidx= 10000
        self.myset= [ListNode(0) for i in range(self.maxidx)]

    def add(self, key: int) -> None:

        index= key%self.maxidx
        curr= self.myset[index]

        while curr.next:
            if curr.next.key== key:
                return
            curr= curr.next

        curr.next= ListNode(key)


    def remove(self, key: int) -> None:
        index= key%self.maxidx
        curr= self.myset[index]

        while curr.next:
            if curr.next.key== key:
                curr.next= curr.next.next
                return
            curr= curr.next
        


    def contains(self, key: int) -> bool:
        index= key%self.maxidx
        curr= self.myset[index]

        while curr.next:
            if curr.next.key== key:
                return True
            curr= curr.next
        return False



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)