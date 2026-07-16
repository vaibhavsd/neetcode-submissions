class Solution:
    def findclosest(self, arr, x, start, end):
        mid= (start+end)//2
        if arr[mid]==x:
            return mid
        elif end-start<=1 and arr[mid]!=x:
            if abs(arr[start]- x) <= abs(arr[end]- x):
                return start
            else:
                return end
        elif arr[mid]<x:
            start= mid
            return self.findclosest(arr, x, start, end)
        else:
            end= mid
            return self.findclosest(arr, x, start, end)

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k==0:
            return []
        from collections import deque
        mydeq= deque()
        idx = self.findclosest(arr, x, 0, len(arr)-1)
        print(f'closest index is {idx}')
        
        mydeq.append(arr[idx])
        backptr= idx-1
        frontptr= idx+1
        total= 1
        while total<k:
            if backptr<0:
                mydeq.append(arr[frontptr])
                frontptr+=1
                total+=1
            elif frontptr>len(arr)-1:
                mydeq.appendleft(arr[backptr])
                total+=1
                backptr-=1
            elif abs(arr[backptr]-x)>abs(arr[frontptr]-x):
                mydeq.append(arr[frontptr])
                frontptr+=1
                total+=1
            else:
                mydeq.appendleft(arr[backptr])
                total+=1
                backptr-=1
        print(mydeq)
        return list(mydeq)
        