class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        res1 = 0
        res2 = 0
        curMax = 0
        curMin = 0
        for num in nums:
            if curMin + num > 0:
                curMin = 0
            else:
                curMin += num
            if curMax + num < 0:
                curMax = 0
            else:
                curMax += num
            res1 = max(res1,curMax)
            res2 = min(res2,curMin)
        if res1 == 0:
            return max(nums)
        if res2 == 0:
            res2 = min(nums)
        return max(res1,sum(nums)-res2)