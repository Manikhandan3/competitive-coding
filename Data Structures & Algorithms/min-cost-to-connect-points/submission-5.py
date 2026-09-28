class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        points = [[p[0],p[1],i] for i,p in enumerate(points)]
        visit = set()
        n = len(points)
        q = [[0,points[0][0],points[0][1],points[0][2]]]
        cost = 0
        while q:
            node = heapq.heappop(q)
            if node[3] in visit:
                continue
            cost += node[0]
            visit.add(node[3])
            for p in points:
                if p[2] not in visit:
                    dist = abs(p[0]-node[1]) + abs(p[1]-node[2])
                    heapq.heappush(q,[dist,p[0],p[1],p[2]])
        return cost
