class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        half = total // 2
        dp = [False] * (half+1)
        dp[0] = True
        for i in range(len(nums)):
            for j in range(half, nums[i]-1, -1):
                dp[j] = dp[j] or dp[j-nums[i]]

        return dp[half]

        # def dfs(i,s):
        #     if s in cache:
        #         return True
            
        #     if s < 0:
        #         return False
            
        #     if i == len(nums):
        #         return False
            
        #     if dfs(i+1,s-nums[i]):
        #         cache.add(s - nums[i])
        #         return True
            
        #     if dfs(i+1,s):
        #         cache.add(s)
        #         return True
            
        #     return False
        
        # return dfs(0,half)