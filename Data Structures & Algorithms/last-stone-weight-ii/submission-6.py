class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)
        target = (stoneSum) // 2
        n = len(stones)
        dp = [[0] * (target+1) for _ in range(n+1)]

        for i in range(n-1,-1,-1):
            for t in range(target+1):
                dp[i][t] = dp[i+1][t]
                if stones[i] <= t:
                     dp[i][t] = max(dp[i][t],stones[i]+dp[i+1][t-stones[i]])
        return stoneSum - 2*dp[0][target]

        # def dfs(i,total):
        #     if i == n:
        #         return 0
        #     if dp[i][total] != 0:
        #         return dp[i][total]
            
        #     res = dfs(i+1,total)
        #     if stones[i] <= total:
        #         res = max(stones[i] + dfs(i+1,total-stones[i]),res)
        #     dp[i][total] = res
        #     return dp[i][total]
        
        # return stoneSum - 2*dfs(0,target)