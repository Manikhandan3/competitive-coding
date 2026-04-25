class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append([r,c])
        directions = [[1,0],[0,1],[0,-1],[-1,0]]
        while q:
            size = len(q)
            for i in range(len(q)):
                node = q.popleft()
                r = node[0]
                c = node[1]
                for d in directions:
                    nr = r + d[0]
                    nc = c + d[1]
                    if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]) or grid[nr][nc] <= grid[r][c]:
                        continue
                    grid[nr][nc] = grid[r][c] + 1
                    q.append([nr,nc])
        
                 
