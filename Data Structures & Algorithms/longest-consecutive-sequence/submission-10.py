class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: 
            nums=set(nums)
            m=0
            for num in nums:
               if (num-1) not in nums:
                   c=0
                   while num in nums:
                       c+=1
                       num+=1
                   m=max(m,c)
            return m
