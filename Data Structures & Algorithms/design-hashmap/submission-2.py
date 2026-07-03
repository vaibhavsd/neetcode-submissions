class Node:
    def __init__(self, key, value=None ):
        self.key= key
        self.value= value
        self.next= None


class MyHashMap:

    def __init__(self):
        self.maxidx= 10000
        self.mytable= [Node(0) for i in range(10000)]

    def put(self, key: int, value: int) -> None:
        idx= key%self.maxidx
        curr= self.mytable[idx]

        while curr.next:
            if curr.next.key== key:
                curr.next.value= value
                return
            curr= curr.next
        curr.next= Node(key, value)

        
    def get(self, key: int) -> int:
        idx= key%self.maxidx
        curr= self.mytable[idx]

        while curr.next:
            if curr.next.key== key:
                return curr.next.value
            curr= curr.next
        return -1
        

    def remove(self, key: int) -> None:
        idx= key%self.maxidx
        curr= self.mytable[idx]

        while curr.next:
            if curr.next.key== key:
                curr.next= curr.next.next
                return
            curr= curr.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)