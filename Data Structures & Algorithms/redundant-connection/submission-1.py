class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges))]
        rank = [1] * len(edges)

        def find(n1):
            while n1 != par[n1]:
                par[n1] = par[par[n1]]
                n1 = par[n1]
            return n1
        
        def union(n1,n2):
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                return False

            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return True

        for n1, n2 in edges:
            if not union(n1-1,n2-1):
                return [n1,n2]
        return [0,0]