class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        N, direct = len(grid), [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c):
            if 0 <= r < N and 0 <= c < N and grid[r][c] == 1:
                grid[r][c] = 2
                q.append((r, c))
                for dr, dc in direct:
                    dfs(r + dr, c + dc)

        q = deque()
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    dfs(r, c)
                    break
            if q: break

        res = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in direct:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < N:
                        if grid[nr][nc] == 1:
                            return res
                        if grid[nr][nc] == 0:
                            grid[nr][nc] = 2
                            q.append((nr, nc))
            res += 1