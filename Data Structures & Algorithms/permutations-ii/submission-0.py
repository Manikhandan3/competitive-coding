class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        visited = [False]*len(nums)

        def dfs(subset):
            if len(subset) == len(nums):
                res.add(tuple(subset))
            
            for i in range(len(nums)):
                if not visited[i]:
                    subset.append(nums[i])
                    visited[i] = True
                    dfs(subset)
                    subset.pop()
                    visited[i] = False
            
        dfs([])
        return [list(s) for s in res] 