class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = math.ceil(len(weights)/days) * l
        res = r

        while l <= r:
            m = (l+r)//2
            d = 1
            s = weights[0]
            for i in range(1,len(weights)):
                if s + weights[i] > m:
                    d += 1
                    s = 0
                s += weights[i]
            if d > days:
                l = m + 1
            else:
                res = m
                r = m - 1
        
        return res

