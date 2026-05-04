class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i in range(len(values)):
            adj[equations[i][0]].append([equations[i][1],values[i]])
            adj[equations[i][1]].append([equations[i][0],1/values[i]])
        
        visited = set()
        res = []
        
        def dfs(num,den,n):
            if num in visited:
                return False
            
            visited.add(num)
            for d in adj[num]:
                if d[0] == den:
                    res.append(n*d[1])
                    visited.remove(num)
                    return True
                elif dfs(d[0],den,n*d[1]):
                    visited.remove(num)
                    return True
            visited.remove(num)
            return False
      
        
        for q in queries:
            if q[0] not in adj or q[1] not in adj:
                res.append(float(-1))
            elif q[0] == q[1]:
                res.append(float(1))
            elif not dfs(q[0],q[1],1):
                res.append(float(-1))
        return res