class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list2= []
        for i in strs:
            list2.append(''.join(sorted(i)))

        list3= set(list2)
        mydict= dict()
        for i in list3:
	        mydict[i]= []

        for i in strs:
            mykey= ''.join(sorted(i))
            mydict[mykey].append(i)

        anslist= []
        for i in mydict.keys():
            anslist.append(mydict[i])
        
        print(anslist)
        return anslist


