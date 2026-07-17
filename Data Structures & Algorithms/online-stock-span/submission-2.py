class StockSpanner:

    def __init__(self):
        self.stack=[]


    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append(price)
            return 1
        sum=1
        elem= -1
        while abs(elem)<=len(self.stack) and self.stack[elem]<=price:
            sum+=1
            elem-=1
        self.stack.append(price)
        return sum


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)