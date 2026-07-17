class MinStack:

    def __init__(self):
        self.mlist= []
        self.minlist= []
        self.minval= []

    def push(self, val: int) -> None:
        self.mlist.append(val)
        if self.minlist:
            self.minlist.append(min(self.minlist[-1], val))
        else:
            self.minlist.append(val)

    def pop(self) -> None:
        self.mlist.pop()
        self.minlist.pop()

    def top(self) -> int:
        return self.mlist[-1]

    def getMin(self) -> int:
        return self.minlist[-1]
        
