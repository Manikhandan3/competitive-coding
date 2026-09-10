class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(i):
            if len(subset) == k:
                res.append(subset.copy())
                return
            
            if i == n+1:
                return
            
            subset.append(i)
            backtrack(i+1)
            subset.pop()
            backtrack(i+1)
        
        backtrack(1)
        return res