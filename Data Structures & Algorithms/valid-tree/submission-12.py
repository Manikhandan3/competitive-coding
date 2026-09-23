class DSU:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.components = n
    
    def find(self,node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self,u,v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        self.components -= 1
        if self.rank[pu] < self.rank[pv]:
            pu, pv = pv, pu
        self.parent[pv] = pu
        self.rank[pu] += self.rank[pv]
        return True
    
    def comps(self):
        return self.components

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        dsu = DSU(n)

        for edge in edges:
            if not dsu.union(edge[0],edge[1]):
                return False
        
        return dsu.comps() == 1
