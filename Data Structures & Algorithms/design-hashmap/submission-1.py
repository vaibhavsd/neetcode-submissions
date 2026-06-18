class MyHashMap:

    def __init__(self):
        self.mkeys= []
        self.mvalues=[]

    def put(self, key: int, value: int) -> None:
        if key in self.mkeys:
            idx= self.mkeys.index(key)
            self.mvalues[idx]= value
        else:
            self.mkeys.append(key)
            self.mvalues.append(value)

    def get(self, key: int) -> int:
        if key in self.mkeys:

            idx= self.mkeys.index(key)
            return self.mvalues[idx]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.mkeys:
            idx= self.mkeys.index(key)
            self.mkeys.pop(idx)
            self.mvalues.pop(idx)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)