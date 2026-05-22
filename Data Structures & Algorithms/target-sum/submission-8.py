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


        def dfs(i, s):
            if s == t:
                return 1

            if s > t or i == len(nums):
                return 0
            
            return dfs(i+1,s) + dfs(i+1,s+nums[i])
        
        return (2**zeros)*dfs(0,0)