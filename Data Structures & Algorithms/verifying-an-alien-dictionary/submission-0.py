class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orders = {}
        for i in range(len(order)):
            orders[order[i]] = i
        for i in range(len(words)-1):
            if len(words[i+1]) <= len(words[i]):
                if words[i][:len(words[i+1])] == words[i+1]:
                    return False
            for j in range(min(len(words[i]),len(words[i+1]))):
                if words[i][j] == words[i+1][j]:
                    continue
                if orders[words[i][j]] >  orders[words[i+1][j]]:
                    return False
                else:
                    break

        return True
                
                

