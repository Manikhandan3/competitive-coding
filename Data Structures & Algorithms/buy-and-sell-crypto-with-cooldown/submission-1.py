class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp = [[-1] * 2 for _ in range(len(prices))]


        def dfs(i,act):
            if i >= len(prices):
                return 0
            
            if dp[i][act] != -1:
                return dp[i][act]
            
            res = 0
            if act == 0:
                res = dfs(i+1,1) - prices[i]
                res = max(dfs(i+1,0),res)
            else:
                res = dfs(i+2,0) + prices[i]
                res = max(dfs(i+1,1),res)
            dp[i][act] = res
            return res
        
        return dfs(0,0)