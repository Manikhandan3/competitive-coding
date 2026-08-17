class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [0] * (len(t)+1)
        dp[len(t)] = 1
        
        for i in range(len(s)-1,-1,-1):
            newdp = [0] * (len(t)+1)
            newdp[len(t)] = 1
            for j in range(len(t)-1,-1,-1):
                newdp[j] = dp[j]
                if s[i] == t[j]:
                    newdp[j] += dp[j+1]
            dp = newdp
        return dp[0]
        # def dfs(i,j):
        #     if j == len(t):
        #         return 1
        #     if i == len(s):
        #         return 0
        #     if dp[i][j] != -1:
        #         return dp[i][j]
        #     if s[i] == t[j]:
        #         dp[i][j] = dfs(i+1,j+1) + dfs(i+1,j)
        #         return dp[i][j]
        #     else:
        #         dp[i][j] = dfs(i+1,j)
        #         return dp[i][j]
        # return dfs(0,0)