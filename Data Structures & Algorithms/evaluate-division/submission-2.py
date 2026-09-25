class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i in range(len(equations)):
            adj[equations[i][0]].append([equations[i][1],values[i]])
            adj[equations[i][1]].append([equations[i][0],1/values[i]])
        
        def dfs(x,y,visited):
            if x not in adj or y not in adj:
                return -1

            if x == y:
                return 1
            visited.add(x)
            for nei, w in adj[x]:
                if nei not in visited:
                    result = dfs(nei, y, visited)
                    if result != -1:
                        return w * result
            return -1
        
        return [dfs(q[0],q[1],set()) for q in queries]