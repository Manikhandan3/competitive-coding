class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0] * (n+1) for _ in range(m+1)]
        memo[m-1][n-1] = 1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i == m - 1 and j == n - 1:
                    continue
                memo[i][j] = memo[i+1][j] + memo[i][j+1]
        return memo[0][0]
        # def dfs(i, j):
        #     if i >= m or j >= n:
        #         return 0
            
        #     if memo[i][j] != -1:
        #         return memo[i][j]
            
        #     memo[i][j] = dfs(i+1,j) + dfs(i,j+1)
        #     return memo[i][j]
        
        # return dfs(0,0)