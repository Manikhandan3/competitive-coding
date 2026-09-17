class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()

        def dfs(i,j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
                return 1
            if (i,j) in visited:
                return 0  
            visited.add((i,j))
            res =  dfs(i+1,j) + dfs(i,j+1) + dfs(i,j-1) + dfs(i-1,j) 
            return res
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] and (m,n) not in visited:
                    res = dfs(m,n)
        
        return res