class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out= [0]*len(temperatures)
        decstack= []
        for idx, val in enumerate(temperatures):
            if idx==0:
                decstack.append((val, idx))
            else:
                if val< decstack[-1][0]:
                    decstack.append((val, idx))
                else:
                    while decstack and decstack[-1][0]<val:
                        elemidx= decstack[-1][1]
                        elem= decstack[-1][0]
                        print(f'{elem}- {elemidx}')
                        out[elemidx]= idx- elemidx
                        decstack.pop()
                    decstack.append((val, idx))
        return out
                    
                