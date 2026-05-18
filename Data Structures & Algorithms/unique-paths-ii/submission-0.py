class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = [[-1] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        memo[len(obstacleGrid)-1][len(obstacleGrid[0])-1] = 1
        def dfs(i,j):
            if i >= len(obstacleGrid) or j >= len(obstacleGrid[0]) or obstacleGrid[i][j] == 1:
                return 0
            
            if memo[i][j] != -1:
                return memo[i][j]
            
            memo[i][j] = dfs(i+1,j) + dfs(i,j+1)
            return memo[i][j]
        
        return dfs(0,0)