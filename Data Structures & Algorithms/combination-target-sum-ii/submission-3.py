class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        candidates.sort()
        
        def dfs(subset,i,total) -> None:
            if total > target:
                return
            if total == target:
                res.add(tuple(subset))
                return 
            if i == len(candidates):
                return
            subset.append(candidates[i])
            dfs(subset,i+1,total+candidates[i])
            subset.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(subset,i+1,total)
        dfs([],0,0)
        return [list(c) for c in res]
