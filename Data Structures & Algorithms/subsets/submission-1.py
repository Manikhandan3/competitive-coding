class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, subset) -> None:
            if i == len(nums):
                res.append(list(subset))
                return 
            
            subset.append(nums[i])
            dfs(i+1,subset)
            subset.pop()
            dfs(i+1,subset)
        dfs(0,[])
        return res