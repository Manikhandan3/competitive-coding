class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = [[grid[0][0],0,0]]
        visit = set()
        time = 0
        while q:
            t, x, y = heapq.heappop(q)
            if (x,y) in visit:
                continue
            if x == m - 1 and y == n - 1:
                return t
            visit.add((x,y))
            for r,c in [[0,1],[1,0],[-1,0],[0,-1]]:
                nr = r + x
                nc = c + y
                if nr < 0 or nr >= m or nc < 0 or nc >= n or (nr,nc) in visit:
                    continue
                heapq.heappush(q,[max(t,grid[nr][nc]),nr,nc])
            