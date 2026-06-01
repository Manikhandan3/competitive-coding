class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0] != 5:
            return False
        hand = {
            20 : 0,
            10 : 0,
            5 : 0
        }
        for bill in bills:
            balance = bill - 5
            while balance:
                temp = balance
                for a in [20,10,5]:
                    if hand[a] > 0 and balance >= a:
                        balance -= a
                        hand[a] -= 1
                        break
                if temp == balance:
                    break
            if balance != 0:
                return False
            hand[bill] += 1
        return True
