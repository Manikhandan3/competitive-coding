class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        for num in hand:
            if not count[num]:
                continue
            start = num
            while count[start - 1] > 0:
                start -= 1
            for i in range(groupSize):
                if not count[start+i]:
                    return False
                count[start+i] -= 1
        return True