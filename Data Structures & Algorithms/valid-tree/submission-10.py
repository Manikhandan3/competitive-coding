class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.comps = n
    
    def find(self,x) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        self.comps -= 1
        if self.rank[pu] < self.rank[pv]:
            pu, pv = pv, pu
        self.parent[pv] = pu
        self.rank[pu] += self.rank[pv]
        return True
    
    def components(self):
        return self.comps
    

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        
        dsu = DSU(n)
        for u,v in edges:
            if not dsu.union(u,v):
                return False
        return True if dsu.components() == 1 else False