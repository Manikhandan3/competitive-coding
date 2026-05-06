class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        #cache = defaultdict(int)
        adj = defaultdict(list)
        ma = {}
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node,parent): 
            m = 0
            for child in adj[node]:
                if child == parent:
                    continue
                m = max(1+dfs(child,node),m)
            return m 
        
        res = float('inf')
        for i in range(n):
            val = dfs(i,-1)
            ma[i] = val
            res = min(res,val)
        r = []
        for k,v in ma.items():
            if v == res:
                r.append(k)
        return r


        

