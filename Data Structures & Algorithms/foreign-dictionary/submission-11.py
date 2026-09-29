class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(set)
        indegree = { c : 0 for word in words for c in word}
        for i in range(len(words)-1):
            src = words[i]
            dst = words[i+1]
            if len(src) > len(dst) and src[:len(dst)] == dst:
                return ""
            for j in range(min(len(src),len(dst))):
                if src[j] == dst[j]:
                    continue
                if dst[j] not in adj[src[j]]:
                    adj[src[j]].add(dst[j])
                    indegree[dst[j]] += 1
                break
        
        q = deque([ i for i in indegree if indegree[i] == 0])
        res = []
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                res.append(node)
                for nei in adj[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)
        return "".join(res) if len(res) == len(indegree) else ""
        

        
