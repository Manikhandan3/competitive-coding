class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        visited = set()
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == 0:
                    q.append([m,n])
        
        while q:
            node = q.popleft()
            for x,y in [[0,1],[1,0],[-1,0],[0,-1]]:
                r = node[0] + x
                c = node[1] + y

                if r < 0 or c < 0 or r >= len(grid) or c >=len(grid[0]) or (r,c) in visited or grid[r][c] <= grid[node[0]][node[1]]:
                    continue
                visited.add((r,c))
                grid[r][c] = grid[node[0]][node[1]] + 1
                q.append([r,c])
        