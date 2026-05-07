class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        q = [[grid[0][0],0,0]]
        res = float('-inf')
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        visited = set()
        while q:
            h, r, c = heapq.heappop(q)
            if (r,c) in visited:
                continue
            visited.add((r,c))
            res = max(h,res)
            if (r,c) == (len(grid)-1,len(grid[0])-1):
                return res
            for d in dirs:
                nr = r + d[0]
                nc = c + d[1]
                if nr >= 0 and nc >= 0 and nr < len(grid) and nc < len(grid[0]) and (nr,nc) not in visited:
                    heapq.heappush(q,[grid[nr][nc],nr,nc])
                
