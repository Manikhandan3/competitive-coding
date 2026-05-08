class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        res = [[0] * k for _ in range(k)]
        rc= defaultdict(list)
        for u, v in rowConditions:
            rc[u].append(v)
        cc= defaultdict(list)
        for u, v in colConditions:
            cc[u].append(v)
        
        visited = {}

        def dfs(node, adj, arr):
            if node in visited:
                return visited[node]
            
            visited[node] = True
            for nei in adj[node]:
                if dfs(nei,adj,arr):
                    return True
            arr.append(node)
            visited[node] = False
            return False

        r = []
        c = []

        for i in range(1,k+1):
            if dfs(i,rc,r):
                return []
        
        visited = {}
        for i in range(1,k+1):
            if dfs(i,cc,c):
                return []
        r.reverse()
        c.reverse()
        for i in range(k):
            for j in range(k):
                if r[i] == c[j]:
                    break
            res[i][j] = r[i]
        
        return res

            
        
