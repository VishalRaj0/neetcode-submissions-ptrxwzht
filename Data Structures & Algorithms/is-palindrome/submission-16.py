class Solution:
    def isAlphaNum(self, c: str) -> bool:
        return (ord('a') <= ord(c) <= ord('z')
        or ord('0') <= ord(c) <= ord('9'))

    def isPalindrome(self, s: str) -> bool:
        normalized = ""
        s = s.lower()
        for c in s:
            if self.isAlphaNum(c):
                normalized += c
        
        return normalized == normalized[::-1]