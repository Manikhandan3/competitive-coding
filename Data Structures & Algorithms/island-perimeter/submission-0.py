class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        visit = set()

        def dfs(r,c):
            nonlocal res

            if (r,c) in visit:
                return 

            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
                res += 1
                return 

            visit.add((r,c))
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    dfs(r,c)
        return res
