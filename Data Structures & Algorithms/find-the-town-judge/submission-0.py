class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        res = trust[0][1]
        people = set(range(1,n+1))

        for t in trust:
            if t[1] != res:
                return -1
            if t[0] in people:
                people.remove(t[0])
        
        if len(people) == 1:
            return res
        return -1