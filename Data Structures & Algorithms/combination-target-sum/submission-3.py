class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(subset, i, s):
            if s > target:
                return
            if s == target:
                res.append(subset.copy())
                return
            if i == len(nums):
                return 
            subset.append(nums[i])
            dfs(subset, i, s + nums[i])
            subset.pop()
            dfs(subset, i+1, s)
        dfs([],0,0)
        return res
