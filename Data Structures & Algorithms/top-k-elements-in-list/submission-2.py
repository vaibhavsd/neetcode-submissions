class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        mydict= defaultdict(int)

        for idx, value in enumerate(nums):
            mydict[value]+=1

        m2= sorted(mydict.items(), key=lambda x:x[1], reverse= True)

        sol= []
        for i in range(k):
            elem1= m2[i]
            elem2= elem1[0]
            sol.append(elem2)
        return sol