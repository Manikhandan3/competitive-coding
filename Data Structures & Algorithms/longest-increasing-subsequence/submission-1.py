class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [1] * n

        for i in range(n-1,-1,-1):
            for j in range(n-1,i,-1):
                if nums[j] > nums[i]:
                    memo[i] = max(1 + memo[j],memo[i])

        return max(memo)

        # def dfs(i):
        #     if memo[i] != -1:
        #         return memo[i]

        #     LIS = 1
        #     for j in range(i + 1, n):
        #         if nums[i] < nums[j]:
        #             LIS = max(LIS, 1 + dfs(j))

        #     memo[i] = LIS
        #     return LIS

        # return max(dfs(i) for i in range(n))