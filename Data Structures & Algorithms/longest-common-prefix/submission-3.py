class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs)<2:
            return strs[0]

        totalstr= len(strs)
        firstword= strs[0]
        count= 0
        for i in range(len(firstword)):
            letter= firstword[i]
            for j in range(len(strs)):
                word= strs[j]
                if len(word)<= i or word[i]!= letter:
                    return firstword[0:count]
            count+=1
        return firstword[0:count] 
