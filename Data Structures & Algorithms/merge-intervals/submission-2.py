class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for s,e in intervals:
            if not res:
                res.append(intervals[0])
            elif s <= res[-1][1]:
                res[-1][1] = max(e, res[-1][1])
            else:
                res.append([s,e])

            
        return res
