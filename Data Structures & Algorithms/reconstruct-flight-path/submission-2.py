class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(adj[src],dst)
        res = []
        
        def dfs(cty):
            while adj[cty]:
                dfs(heapq.heappop(adj[cty]))
            res.append(cty)

        dfs("JFK")
        res.reverse()
        return res
