class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        sol= [0]*len(temperatures)
        for i in range(len(temperatures)):
            today= temperatures[i]
            
            for j in range(i+1, len(temperatures)):
                if temperatures[j]>today:
                    sol[i]=j-i
                    break  
        return sol