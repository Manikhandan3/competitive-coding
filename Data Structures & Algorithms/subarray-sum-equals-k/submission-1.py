class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {}
        prefixSum[0] = 1
        s = 0
        res = 0
        for num in nums:
            s += num
            diff = s - k
            res += prefixSum.get(diff,0)
            prefixSum[s] = 1 + prefixSum.get(s,0)
        return res
