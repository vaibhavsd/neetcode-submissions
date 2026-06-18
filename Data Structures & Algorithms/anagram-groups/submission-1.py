class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter
        myset= list()
        freqdict= defaultdict(list)

        for i in strs:
            j= "".join(sorted(i))
            freqdict[j].append(i)

        return list(freqdict.values())
        

