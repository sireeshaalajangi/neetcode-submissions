class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        for i in range(n):
            for j in range(n):
                if(numbers[i]+numbers[j]==target and i<j):
                    return [i+1,j+1]