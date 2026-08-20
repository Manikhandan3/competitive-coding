class Solution:
    def mySqrt(self, x: int) -> int:
        r = (x+1) // 2
        l = 0
        res = 0
        while l <= r:
            m = (l+r) // 2
            if m * m <=  x:
                res = m
                l = m + 1
            else:
                r = m - 1
        return res