class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        # get closest index 

        # index+k, index-j, k++, j++

        mlist= []
        for i in arr:
            mlist.append(abs(i-x))
        mdict= dict()
        print(mlist)

        for idx, val in enumerate(mlist):
            mdict[idx]= val
        print(mdict)
        sorteddict= sorted(mdict.items(), key= lambda x:x[1])

        print(sorteddict)

        mans=[]
        for i in range(k):
            mans.append(arr[sorteddict[i][0]])
        return sorted(mans)