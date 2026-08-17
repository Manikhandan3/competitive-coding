class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        res = float('inf')
        s = 0
        for r in range(len(nums)):
            s += nums[r]
            while s - nums[l] >= target:
                s -= nums[l]
                l += 1
            if s >= target:
                res = min(res,r-l+1)
        return 0 if res == float('inf') else res