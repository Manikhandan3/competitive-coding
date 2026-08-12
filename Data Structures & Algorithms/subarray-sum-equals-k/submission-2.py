class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preMap = defaultdict(int)
        preMap[0] = 1
        s = 0
        res = 0
        for n in nums:
            s += n
            res += preMap[s - k]
            preMap[s] += 1
        
        return res