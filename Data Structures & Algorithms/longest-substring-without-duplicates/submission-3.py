class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        m=0
        left=0
        right=0
        seen=set()
        while(right<n):
            if s[right] not in seen:
                seen.add(s[right])
                right+=1
                m=max(m,right-left)
            else:
                seen.remove(s[left])
                left+=1
                
        return m

