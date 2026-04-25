class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append([r,c])
                if grid[r][c] == 1:
                    fresh += 1
        directions = [[1,0],[0,1],[0,-1],[-1,0]]
        time = 0
        while q and fresh:
            time += 1
            size = len(q)
            for i in range(len(q)):
                node = q.popleft()
                r = node[0]
                c = node[1]
                for d in directions:
                    nr = r + d[0]
                    nc = c + d[1]
                    if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]) or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append([nr,nc])
        return time if fresh == 0 else -1