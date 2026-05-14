class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        half = total // 2
        cache = { 0 : True}

        def dfs(i,s):
            if s in cache:
                return cache[s]
            
            if s < 0:
                return False
            
            if i == len(nums):
                return False
            
            if dfs(i+1,s-nums[i]):
                cache[s - nums[i]] = True
                return True
            
            if dfs(i+1,s):
                cache[s] = True
                return True
            
            return False
        
        return dfs(0,half)