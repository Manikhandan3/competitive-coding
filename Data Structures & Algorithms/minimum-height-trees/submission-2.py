class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        indegree = [0] * n
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
            indegree[x] += 1
            indegree[y] += 1
        
        q = deque([i for i in range(len(indegree)) if indegree[i] <= 1])
        while n > 2:
            # print(q)
            for _ in range(len(q)):
                node = q.popleft()
                n -= 1
                for nei in adj[node]:
                    indegree[nei] -= 1
                    # print(indegree)
                    if indegree[nei] == 1:
                        q.append(nei)

        return list(q)
