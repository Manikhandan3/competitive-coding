class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        while l < r:
            m = (l + r) // 2
            time = 0

            for pile in piles:
                time = time + math.ceil(pile/m)
            if time > h:
                l = m + 1
            else:
                res = m
                r = m 
        return res
