class StockSpanner:

    def __init__(self):
        self.stack=[]


    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append((price, 1))
            return 1
        if self.stack[-1][0]>price:
            self.stack.append((price, 1))
            return 1
        else:
            sum=1
            elem= -1
            while abs(elem)<=len(self.stack) and self.stack[elem][0]<= price:
                elemspan=self.stack[elem][1]
                sum+=elemspan
                elem-=elemspan
                #print(f'Moved back {elemspan} elems for {price}')
            self.stack.append((price, sum))
        return sum
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)