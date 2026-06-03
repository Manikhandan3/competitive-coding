class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        count = Counter(senate)
        if 'R' not in count:
            return "Dire"
        if 'D' not in count:
            return "Radiant"
        r = 0
        d = 0
        while True:
            for i in range(len(senate)):
                if r > 0 and senate[i] == 'D':
                    senate[i] == 'A'
                    r -= 1
                elif d > 0 and senate[i] == 'R':
                    senate[i] == 'A'
                    d -= 1
                elif senate[i] == 'R':
                    r += 1
                    count['D'] -= 1
                    if count['D'] == 0:
                        return "Radiant"
                elif senate[i] == 'D':
                    d += 1
                    count['R'] -= 1
                    if count['R'] == 0:
                        return "Dire"
                