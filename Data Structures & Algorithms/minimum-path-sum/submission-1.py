class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp =[[-1]*len(grid[0]) for _ in range(len(grid))]
        dp[len(grid)-1][len(grid[0])-1] = grid[len(grid)-1][len(grid[0])-1]
        def dfs(i,j):
            if i >= len(grid) or j >= len(grid[0]):
                return float('inf')

            if dp[i][j] != -1:
                return dp[i][j]
            
            dp[i][j] = grid[i][j] + min(dfs(i+1,j),dfs(i,j+1))
            return dp[i][j]
        return dfs(0,0)
