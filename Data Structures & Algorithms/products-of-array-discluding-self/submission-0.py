class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        arr=[0]*n
        for i in range(n):
            k=1
            for j in range(n):
                if i==j:
                    arr[i]=k
                elif i!=j:
                    k=k*nums[j]
                    arr[i]=k
            
        return arr
    

