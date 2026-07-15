class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n=len(nums)
        count=1
        m=1
        nums1=sorted(nums)
        for j in range(1,n):
            if(nums1[j]-nums1[j-1]==1):
                count+=1
            elif(nums1[j]==nums1[j-1]):
                continue
            else:
                count=1
            m=max(m,count)
        return m