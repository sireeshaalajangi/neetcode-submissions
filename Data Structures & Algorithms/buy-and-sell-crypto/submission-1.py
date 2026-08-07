class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=0;
        n=len(prices)
        for i in range(n):
            for j in range(i,n):
                p=(prices[j]-prices[i])
                m=max(p,m)
        return m