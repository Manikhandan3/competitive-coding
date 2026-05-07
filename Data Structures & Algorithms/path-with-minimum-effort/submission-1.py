class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        minHeap = [[0,0,0]]
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        visited = set()
        while minHeap:
            node = heapq.heappop(minHeap)
            if (node[1],node[2]) in visited:
                continue
            visited.add((node[1],node[2]))
            if node[1] == len(heights)-1 and node[2] == len(heights[0])-1:
                return node[0]
            for d in dirs:
                r = node[1] + d[0]
                c = node[2] + d[1]
                if r >= 0 and c >= 0 and r < len(heights) and c < len(heights[0]) and (r,c) not in visited:
                    newDiff = max(node[0], abs(heights[r][c] - heights[node[1]][node[2]]))
                    heapq.heappush(minHeap,[newDiff,r,c])
        return -1
                