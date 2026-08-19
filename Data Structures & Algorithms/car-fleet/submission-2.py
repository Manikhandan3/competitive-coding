class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position,speed)]
        pair.sort(reverse=True)
        fleet = 1
        time = (target - pair[0][0])/pair[0][1]
        for i in range(1,len(pair)):
            t = (target - pair[i][0])/pair[i][1]
            if t > time:
                fleet += 1
                time = t
        return fleet