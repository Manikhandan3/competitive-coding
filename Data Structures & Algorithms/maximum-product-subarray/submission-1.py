class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        max_p, min_p = 1, 1

        for n in nums:
            tmp = max_p * n
            max_p = max(n*max_p, n*min_p, n)
            min_p = min(tmp, n*min_p, n)
            res = max(res,max_p)
        return res