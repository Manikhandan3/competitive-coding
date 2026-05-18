class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c : set() for w in words for c in w}
        for i in range(len(words)-1):
            if len(words[i]) > len(words[i+1]) and words[i][:len(words[i+1])]==words[i+1]:
                return "" 
            for c in range(min(len(words[i]),len(words[i+1]))):
                if words[i][c]!=words[i+1][c]:
                    adj[words[i][c]].add(words[i+1][c])
                    break
        visited = {}
        res = []

        def dfs(c):
            if c in visited:
                return visited[c]
            
            visited[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True
            visited[c] = False
            res.append(c)
            return False
        
        for char in adj:
            if dfs(char):
                return ""
        res.reverse()
        return "".join(res)
        