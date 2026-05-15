class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        cache = { 0 : 1}

        def dfs(total):
            if total in cache:
                return cache[total]
            
            res = 0
            for i in range(len(nums)):
                if total < nums[i]:
                    break
                res += dfs(total - nums[i])
                cache[total] = res
            return res
        
        return dfs(target)