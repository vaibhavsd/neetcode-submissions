class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        minlen= min(len(strs[0]), len(strs[-1]))

        strs1= strs[0]
        strs2= strs[-1]
        lcf= ""
        for i in range(minlen):
            if  strs1[i]==strs2[i]:
                lcf+=(strs1[i])
            else:
                break
        return lcf