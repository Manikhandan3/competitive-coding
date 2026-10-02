class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0] * (len(nums)+1)
        dp[len(nums)-1] = nums[-1]
        dp[len(nums)-2] = nums[-2]
        for i in range(len(nums)-3,-1,-1):
            dp[i] = nums[i] + max(dp[i+3],dp[i+2])
        
        return max(dp[0],dp[1])