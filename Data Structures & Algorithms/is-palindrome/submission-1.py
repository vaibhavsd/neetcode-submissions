class Solution:
    def isPalindrome(self, s: str) -> bool:
        snew= "".join([i for i in s if i.isalnum()])
        snew2= snew.lower()
        print(snew2)
        snew3= snew2[::-1]
        return snew3==snew2