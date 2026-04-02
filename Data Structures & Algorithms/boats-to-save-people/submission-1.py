class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l = 0
        r = len(people)-1
        res = 0
        people.sort()
        while l<=r:
            if l<=r and people[l]+people[r]>limit:
                res += 1
                r -= 1
            else:
                res += 1
                l += 1
                r -= 1
        return res