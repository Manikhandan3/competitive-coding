class DSU:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.n = n
    
    def find(self,n):
        if self.parent[n] != n:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]
    
    def union(self,u,v):
        pu = self.find(u)
        pv = self.find(v)
        if pv == pu:
            return False
        self.n -= 1
        if self.rank[pv] > self.rank[pu]:
            pu, pv = pv, pu
        self.parent[pv] = pu
        self.rank[pu] += self.rank[pv]
        return True
    
    def isConnected(self):
        return self.n == 1

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edges = [e + [i] for i,e in enumerate(edges)]
        edges.sort(key=lambda x: x[2])
        
        def findMST(index, include):
            uf = DSU(n)
            wgt = 0
            if include:
                wgt += edges[index][2]
                uf.union(edges[index][0], edges[index][1])
            for i, e in enumerate(edges):
                if i == index:
                    continue
                if uf.union(e[0], e[1]):
                    wgt += e[2]
            return wgt if uf.isConnected() else float("inf")
        
        mst_wgt = findMST(-1, False)
        critical, pseudo = [], []
        for i, e in enumerate(edges):
            if mst_wgt < findMST(i, False):
                critical.append(e[3])
            elif mst_wgt == findMST(i, True):
                pseudo.append(e[3])

        return [critical, pseudo]
                
        