class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        adj_row = defaultdict(list)
        adj_col = defaultdict(list)
        for u,v in rowConditions:
            adj_row[u].append(v)
        for u,v in colConditions:
            adj_col[u].append(v)
        rows = []
        cols = []

        def dfs(i,ans,visit,adj):
            if i in visit:
                return visit[i]
            
            visit[i] = True
            for nei in adj[i]:
                if dfs(nei,ans,visit,adj):
                    return True
            visit[i] = False
            ans.append(i)
            return False
        
        vr = {}
        vc = {}
        for j in range(1,k+1):
            if dfs(j,rows,vr,adj_row) or dfs(j,cols,vc,adj_col):
                return []
        rows.reverse()
        cols.reverse()
        # print(rows,cols)
        res = [[0] * k for _ in range(k)]

        for i,r in enumerate(rows):
            res[i][cols.index(rows[i])] = rows[i]
        return res
        
