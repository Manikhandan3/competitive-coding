class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        val = set()
        res = 0
        for num in nums:
            val.add(num)
        for v in val:
            if (v-1) not in val:
                l = 1
                while (v + l) in val:
                    l += 1
                res = max(l,res)
        return res

