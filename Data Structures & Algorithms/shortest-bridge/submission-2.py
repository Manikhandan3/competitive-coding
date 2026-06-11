class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        N, direct = len(grid), [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q2 = deque()

        found = False
        for r in range(N):
            if found: break
            for c in range(N):
                if grid[r][c] == 1:
                    q1 = deque([(r, c)])
                    grid[r][c] = 2
                    while q1:
                        x, y = q1.popleft()
                        q2.append((x, y))
                        for dx, dy in direct:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == 1:
                                grid[nx][ny] = 2
                                q1.append((nx, ny))
                    found = True
                    break

        res = 0
        while q2:
            for _ in range(len(q2)):
                x, y = q2.popleft()
                for dx, dy in direct:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N:
                        if grid[nx][ny] == 1:
                            return res
                        if grid[nx][ny] == 0:
                            grid[nx][ny] = 2
                            q2.append((nx, ny))
            res += 1

        return res