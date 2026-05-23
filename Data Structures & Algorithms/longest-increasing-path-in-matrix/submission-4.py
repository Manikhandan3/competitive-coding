class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
        dp = [[-1] * len(matrix[0]) for _ in range(len(matrix))]
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        ans = 1

        def dfs(i,j):
            if dp[i][j] != -1:
                return dp[i][j]
            
            res = 1
            visited[i][j] = True
            for d in dirs:
                nr = i + d[0]
                nc = j + d[1]
                if nr >= 0 and nc >= 0 and nr < len(matrix) and nc < len(matrix[0]) and not visited[nr][nc] and matrix[nr][nc] > matrix[i][j]:
                    res = max(res, 1 + dfs(nr,nc))

            visited[i][j] = False
            dp[i][j] = res
            return dp[i][j]

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                dp[r][c]=dfs(r,c)
                ans = max(ans,dp[r][c])
        return ans