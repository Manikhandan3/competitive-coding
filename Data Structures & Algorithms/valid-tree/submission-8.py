class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(n)}
        for n1, n2 in edges:
            preMap[n1].append(n2)
            preMap[n2].append(n1)
        
        visited = set()

        def dfs(i, parent):
            if i in visited:
                return False
            
            visited.add(i)
            for child in preMap[i]:
                if child == parent:
                    continue
                if not dfs(child, i):
                    return False
            
            return True
        
        return dfs(0,-1) and len(visited) == n