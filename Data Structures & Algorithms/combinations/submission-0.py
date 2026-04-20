class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        l = list(range(1,n+1))
        res = []
        
        def dfs(subset, i, k):
            if len(subset) == k:
                res.append(subset.copy())
                return
            if i == n:
                return
            subset.append(l[i])
            dfs(subset,i+1,k)
            subset.pop()
            dfs(subset,i+1,k)
        dfs([],0,k)
        return res
