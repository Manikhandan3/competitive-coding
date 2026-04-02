class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        m = prices[0]
        for p in prices:
            profit = p - m
            m = min(m,p)
            res = max(res,profit)
        return res