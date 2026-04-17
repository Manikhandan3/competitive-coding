class Solution:
    def reorganizeString(self, s: str) -> str:
        res = []
        count = Counter(s)
        c = []
        for key in count:
            c.append([-count[key],key])
        heapq.heapify(c)
        lu = ""
        lcnt = 0
        while c:
            cnt, l = heapq.heappop(c)
            # if l == lu:
            #     return ""
            cnt += 1
            res.append(l)
            if lu and lcnt:
                heapq.heappush(c,[lcnt, lu])
            lu = l
            lcnt = cnt
        
        if len(res) != len(s):
            return ""
        return "".join(res)



