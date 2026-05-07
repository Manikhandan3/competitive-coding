class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,t in times:
            adj[u].append([v,t])
        visit = set()
        q = [(0,k)]
        time = 0
        while q:
            node = heapq.heappop(q)
            if node[1] in visit:
                continue
            visit.add(node[1])
            time = node[0]
            for nei in adj[node[1]]:
                if nei[0] not in visit:
                    heapq.heappush(q,[node[0]+nei[1],nei[0]])
        return time if len(visit) == n else -1

