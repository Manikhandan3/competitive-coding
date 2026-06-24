class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = []
        for k,v in count.items():
            if v == 1:
                res.append(k)
        return res