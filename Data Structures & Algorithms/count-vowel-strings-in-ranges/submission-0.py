class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        preSum = [0] * len(words)
        for i,word in enumerate(words):
            if i > 0: preSum[i] = preSum[i-1]
            if word.startswith(('a','i','e','o','u')) and word.endswith(('a','i','e','o','u')):
                if i > 0:
                    preSum[i] += 1
                else:
                    preSum[i] = 1
        res = [0] * len(queries)
        for x,y in enumerate(queries):
            if y[0] == 0:
                res[x] = preSum[y[1]]
            else:
                res[x] = preSum[y[1]] - preSum[y[0]-1]
        return res