class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        m = prices[0]
        for p in prices:
            res = max(res,p-m)
            m = min(m,p)
        return res