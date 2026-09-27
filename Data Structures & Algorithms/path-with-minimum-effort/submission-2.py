class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        q = [[0,0,0]]
        visit = set()
        m = len(heights)
        n = len(heights[0])
        while q:
            h, x, y = heapq.heappop(q)
            if (x,y) in visit:
                continue
            if x == m - 1 and y == n - 1:
                return h
            visit.add((x,y))
            for r,c in [[0,1],[1,0],[-1,0],[0,-1]]:
                nr = x + r
                nc = y + c
                if nr < 0 or nc < 0 or nr >= m or nc >= n or (nr,nc) in visit:
                    continue
                diff = abs(heights[x][y]-heights[nr][nc])
                heapq.heappush(q,[max(h,diff),nr,nc])
                
