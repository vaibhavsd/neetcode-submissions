class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<2:
            return nums
        mylen= len(nums)

        firsthalf= self.sortArray(nums[0: mylen//2])
        secondhalf= self.sortArray(nums[mylen//2: mylen])
        
        secondlen= mylen- mylen//2
        start1= 0
        start2= 0
        st1max= mylen//2
        st2max= secondlen
        idx=0
        mergearr=[]
        while start1<st1max or start2<st2max:
            if start1>=st1max and start2<st2max:
                mergearr.append(secondhalf[start2])
                start2+=1

            elif start2>=st2max and start1<st1max:
                mergearr.append(firsthalf[start1])
                start1+=1

            elif firsthalf[start1]<secondhalf[start2]:
                mergearr.append(firsthalf[start1])
                start1+=1

            elif firsthalf[start1]>=secondhalf[start2]:
                mergearr.append(secondhalf[start2])
                start2+=1
            idx+=1

        return mergearr