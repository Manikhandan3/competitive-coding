class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = [False]*len(nums)

        def dfs(subset):
            if len(subset) == len(nums):
                res.append(subset.copy())
            
            for i in range(len(nums)):
                if not visited[i]:
                    subset.append(nums[i])
                    visited[i] = True
                    dfs(subset)
                    subset.pop()
                    visited[i] = False
            
        dfs([])
        return res
