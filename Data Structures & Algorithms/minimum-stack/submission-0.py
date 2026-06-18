class MinStack:

    def __init__(self):
        self.mystack=deque()
        self.minstack=deque()
        
    def push(self, val: int) -> None:
        self.mystack.append(val)
        if self.minstack:
            minval= min(val, self.minstack[-1])
        else:
            minval= val
        self.minstack.append(minval)

    def pop(self) -> None:
        self.mystack.pop()
        self.minstack.pop()


    def top(self) -> int:
        return self.mystack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
        
