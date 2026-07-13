class Solution:
    def isPalindrome(self, s: str) -> bool:
        ls = ''.join(ch.lower() for ch in s if ch.isalnum())
        n=len(ls)
        i=0
        for i in range(n//2):
            if ls[i]!=ls[n-1-i]:
                return False
        return True
        