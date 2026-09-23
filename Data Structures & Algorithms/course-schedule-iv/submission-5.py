class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for _ in range(numCourses)]
        for x,y in prerequisites:
            adj[y].append(x)
        cache = [[-1] * numCourses for _ in range(numCourses)]
        
        def dfs(i,j):
            if i == j:
                return True
            
            if cache[i][j] != -1:
                return cache[i][j]
        
            for nei in adj[j]:
                if dfs(i,nei):
                    cache[i][j] = 1
                    return True
            cache[i][j] = 0
            return False
        
        res = [False] * len(queries)
        for i in range(len(queries)):
            if dfs(queries[i][0],queries[i][1]):
                res[i] = True
        return res

            