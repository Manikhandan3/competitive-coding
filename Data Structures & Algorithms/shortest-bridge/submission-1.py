class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, node):
        cur = node
        while cur != self.parent[cur]:
            self.parent[cur] = self.parent[self.parent[cur]]
            cur = self.parent[cur]
        return cur

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.rank[pv] > self.rank[pu]:
            pu, pv = pv, pu
        self.parent[pv] = pu
        self.rank[pu] += self.rank[pv]
        return True

class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        n, direct = len(grid), [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dsu = DSU(n * n + 1)

        def idx(r, c):
            return r * n + c + 1

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    first_island = dsu.find(idx(r, c))
                    if c + 1 < n and grid[r][c + 1] == 1:
                        dsu.union(idx(r, c), idx(r, c + 1))
                    if r + 1 < n and grid[r + 1][c] == 1:
                        dsu.union(idx(r, c), idx(r + 1, c))

        q = deque()
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    if dsu.find(idx(r, c)) != first_island:
                        continue
                    for dx, dy in direct:
                        nr, nc = r + dx, c + dy
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                            q.append((r,c))
                            break

        res = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dx, dy in direct:
                    nr, nc = r + dx, c + dy
                    if 0 <= nr < n and 0 <= nc < n:
                        if grid[nr][nc] == 1 and dsu.union(idx(r, c), idx(nr, nc)):
                            return res
                        if grid[nr][nc] == 0:
                            grid[nr][nc] = 1
                            dsu.union(idx(r, c), idx(nr, nc))
                            q.append((nr, nc))
            res += 1