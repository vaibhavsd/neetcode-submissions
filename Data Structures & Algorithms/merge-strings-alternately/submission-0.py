class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word3= ''
        ptr1= 0
        ptr2= 0
        while ptr1<=len(word1)-1 or ptr2<=len(word2)-1:
            if ptr1<=len(word1)-1:
                word3+=word1[ptr1]
                ptr1+=1
            if ptr2<=len(word2)-1:
                word3+=word2[ptr2]
                ptr2+=1
        return word3