class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n, node = len(points), 0
        visit = [False] * n
        dist = [10000000] * n
        edges, cost = 0, 0
        while edges < n - 1:
            visit[node] = True
            nextNode = -1

            for i in range(n):
                if visit[i]:
                    continue
                cur = (abs(points[i][0] - points[node][0]) +
                           abs(points[i][1] - points[node][1]))
                dist[i] = min(dist[i],cur)
                if nextNode == -1 or dist[i] < dist[nextNode]:
                    nextNode = i
                    
            cost += dist[nextNode]
            node = nextNode
            edges += 1
        return cost
