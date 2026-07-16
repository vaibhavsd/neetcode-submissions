class MyQueue:

    def __init__(self):
        self.inputstack= []
        self.outputstack= []

    def push(self, x: int) -> None:
        self.inputstack.append(x)

    def pop(self) -> int:
        
        if self.outputstack:
            return self.outputstack.pop()
        else:
            while self.inputstack:
                self.outputstack.append(self.inputstack.pop())
            return self.outputstack.pop()

    def peek(self) -> int:
        if self.outputstack:
            return self.outputstack[-1]
        else:
            while self.inputstack:
                self.outputstack.append(self.inputstack.pop())
            return self.outputstack[-1]


    def empty(self) -> bool:
        if not self.inputstack and not self.outputstack:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()