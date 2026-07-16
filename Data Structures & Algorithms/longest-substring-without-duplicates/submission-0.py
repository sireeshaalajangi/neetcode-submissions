class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m=0
        n=len(s)
        for i in range(n):
            seen=set()
            count=0
            for j in range(i,n):
                if s[j] not in seen:
                    seen.add(s[j])
                    count+=1
                else:
                    break;
            m=max(m,count)
        return m