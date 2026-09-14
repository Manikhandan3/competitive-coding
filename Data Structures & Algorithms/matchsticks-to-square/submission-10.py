class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        length = sum(matchsticks)
        if length % 4:
            return False
        length = length // 4
        sides = [0] * 4
        matchsticks.sort(reverse=True)
        if matchsticks[0] > length:
            return False

        def backtrack(i):
            if i == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sides[3]
            for side in range(4):
                if sides[side] + matchsticks[i] > length:
                    continue
                sides[side] += matchsticks[i]
                if backtrack(i+1):
                    return True
                sides[side] -= matchsticks[i]
            return False
        
        return backtrack(0)

