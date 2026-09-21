class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0]) 
        pac = [[False] * n for _ in range(m)]
        atl = [[False] * n for _ in range(m)]

        def dfs(r, c, sea, prev):
            if r < 0 or c < 0 or r >= m or c >= n or sea[r][c] or heights[r][c] < prev:
                return
            
            sea[r][c] = True
            dfs(r + 1, c, sea, heights[r][c])
            dfs(r - 1, c, sea, heights[r][c])
            dfs(r, c + 1, sea, heights[r][c])
            dfs(r, c - 1, sea, heights[r][c])
        
        for c in range(n):
            dfs(0, c, pac, heights[0][c])
            dfs(m - 1, c, atl, heights[m - 1][c])

        for r in range(m):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, n - 1, atl, heights[r][n - 1])
        
        res = []
        for r in range(m):
            for c in range(n):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])
        return res