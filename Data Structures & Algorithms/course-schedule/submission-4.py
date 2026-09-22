class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]

        for pre in prerequisites:
            if pre[1] == pre[0]:
                return False
            adj[pre[0]].append(pre[1])
        visited = {}
        def dfs(i):
            if i in visited:
                return visited[i]
            
            visited[i] = True
            for child in adj[i]:
                if dfs(child):
                    return False
            visited[i] = False
            return False
        
        for n in range(numCourses):
            if dfs(n):
                return False
        return True
        