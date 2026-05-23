class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        zeros = 0
        for num in nums:
            if num == 0:
                zeros += 1
        total = sum(nums)
        nums = [x for x in nums if x != 0]
        if (total+target) % 2:
            return 0
        t = (total+target)//2
        dp = [[0] * (t+1) for _ in range(len(nums)+1)]
        for k in range(len(nums)+1):
            dp[k][0] = 1

        for i in range(len(nums)-1,-1,-1):
            for s in range(t+1):
                if s >= nums[i]:
                    dp[i][s] = dp[i+1][s] + dp[i+1][s-nums[i]]
                else:
                    dp[i][s] = dp[i+1][s]
        return dp[0][t]*(2**zeros)

        # def dfs(i, s):
        #     if s == t:
        #         return 1

        #     if s > t or i == len(nums):
        #         return 0
            
        #     if dp[i][s] != -1:
        #         return dp[i][s]
            
        #     dp[i][s] = dfs(i+1,s) + dfs(i+1,s+nums[i])
        #     return dp[i][s]
        # return (2**zeros)*dfs(0,0)