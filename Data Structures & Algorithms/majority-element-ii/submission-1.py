class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        totalelem= len(nums)
        maxcount= totalelem/3
        mydict= dict()
        outlist= []
        for i in nums:
            if i not in mydict.keys():
                mydict[i]= 1
                if mydict[i] > maxcount:
                    if i not in outlist:
                        outlist.append(i)
                        
            else:
                mydict[i] += 1

                if mydict[i] > maxcount:
                    if i not in outlist:
                        outlist.append(i)
        print(mydict)
        return outlist

        
        