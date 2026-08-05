class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=""
        for c in s:
            if(c.isalnum()):
                st+=c.lower()
        l=len(st)
        for i in range(l//2):
            if(st[i]!=st[l-1-i]):
                return False
            else:
                continue
        return True
        