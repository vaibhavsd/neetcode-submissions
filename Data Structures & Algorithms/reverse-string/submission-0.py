class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        elems= len(s)
        for i in range(int(elems/2)):
            s[i], s[elems-1-i]= s[elems-1-i], s[i]
         