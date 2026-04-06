class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        r = math.ceil(len(nums)/k) * l
        res = r
        while l <= r:
            m = (l+r)//2
            s = 0
            c = 1
            for i in range(len(nums)):
                if s + nums[i] > m:
                    c += 1
                    s = 0
                s += nums[i]
            if c > k:
                l = m + 1
            else:
                res = m
                r = m - 1

        return res

