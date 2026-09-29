class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        price = [100001] * n
        adj = [[] for _ in range(n)]
        for u,v,p in flights:
            adj[u].append([v,p])
        price[src] = 0
        q = deque([[0,src,0]])
        while q:
            cost, node, stops = q.popleft()
            if stops > k:
                continue
            for nei, w in adj[node]:
                if price[nei] > cost+w:
                    q.append([cost + w,nei, stops + 1])
                    price[nei] = cost + w

        return -1 if price[dst] == 100001 else price[dst]

        