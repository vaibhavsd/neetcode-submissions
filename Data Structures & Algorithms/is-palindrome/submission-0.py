class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        news = ''.join(filter(str.isalnum, s))
        news= news.lower()
        reverses= news[::-1]
        return news== reverses