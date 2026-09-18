class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        res = 0

        def dfs(i,j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or (i,j) in visited or grid[i][j] == 0:
                return 0

            visited.add((i,j))
            return 1 + dfs(i+1,j) + dfs(i-1,j) + dfs(i,j+1) + dfs(i,j-1)
        
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == 1 and (m,n) not in visited:
                    res = max(res,dfs(m,n))
        return res