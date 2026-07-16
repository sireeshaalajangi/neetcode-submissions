class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=0
        n=len(prices)
        for i in range(n):
            for j in range(i+1,n):
                max1=(prices[j]-prices[i])
                m=max(m,max1)
        return m