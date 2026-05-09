class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        memo = [[0] * 2 for _ in range(len(nums)+2)]

        for i in range(len(nums)-1,0,-1):
            memo[i][1] = max(memo[i+1][1], nums[i]+memo[i+2][1])
            memo[i-1][0] = max(memo[i][0], nums[i-1]+memo[i+1][0])
        
        return max(memo[0][0],memo[1][1])

        # def dfs(i, flag):
        #     if i >= len(nums) or (flag and i == len(nums) - 1):
        #         return 0
        #     if memo[i][flag] != -1:
        #         return memo[i][flag]
        #     memo[i][flag] = max(dfs(i + 1, flag),
        #                     nums[i] + dfs(i + 2, flag or (i == 0)))
        #     return memo[i][flag]

        # return max(dfs(0, True), dfs(1, False))