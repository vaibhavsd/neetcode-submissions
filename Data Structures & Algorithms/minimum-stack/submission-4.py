class MinStack:
    import math
    def __init__(self):
        self.mlist= []
        self.minlist= []
        self.minelem= math.inf

    def push(self, val: int) -> None:
        self.mlist.append(val)
        if val<self.minelem:
            self.minelem= val
        self.minlist.append(self.minelem)

    def pop(self) -> None:
        self.mlist.pop()
        self.minlist.pop()
        if self.minlist:
            self.minelem= self.minlist[-1]
        else:
            self.minelem= math.inf
    def top(self) -> int:
        return self.mlist[-1]

    def getMin(self) -> int:
        return self.minlist[-1]

        
