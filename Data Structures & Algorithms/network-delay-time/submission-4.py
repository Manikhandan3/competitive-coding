class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,t in times:
            adj[u].append([v,t])
        time = 0
        q = [[0,k]]
        visit = set()
        while q:
            node = heapq.heappop(q)
            if node[1] in visit:
                continue
            visit.add(node[1])
            if len(visit) == n:
                return node[0]
            for nei in adj[node[1]]:
                if nei[0] not in visit:
                    heapq.heappush(q,[nei[1]+node[0],nei[0]])
        return -1

            
            