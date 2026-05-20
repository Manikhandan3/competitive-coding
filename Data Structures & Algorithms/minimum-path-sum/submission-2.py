class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp =[[float('inf')]*(len(grid[0])+1) for _ in range(len(grid)+1)]
        dp[len(grid)-1][len(grid[0])-1] = grid[len(grid)-1][len(grid[0])-1]
        
        for i in range(len(grid)-1,-1,-1):
            for j in range(len(grid[0])-1,-1,-1):
                if i == len(grid)-1 and j == len(grid[0])-1:
                    continue
                dp[i][j] = grid[i][j] + min(dp[i+1][j],dp[i][j+1])
        return dp[0][0]

        # def dfs(i,j):
        #     if i >= len(grid) or j >= len(grid[0]):
        #         return float('inf')

        #     if dp[i][j] != -1:
        #         return dp[i][j]
            
        #     dp[i][j] = grid[i][j] + min(dfs(i+1,j),dfs(i,j+1))
        #     return dp[i][j]
        # return dfs(0,0)
