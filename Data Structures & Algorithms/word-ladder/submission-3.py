class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 0
        
        if len(beginWord) != len(endWord):
            return 0
        
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        
        qb, qe = deque([beginWord]), deque([endWord])
        fromBegin, fromEnd = {beginWord: 1}, {endWord: 1}

        while qb and qe:
            if len(qb) > len(qe):
                qb, qe = qe, qb
                fromBegin, fromEnd = fromEnd, fromBegin
            for _ in range(len(qb)):
                word = qb.popleft()
                steps = fromBegin[word]
                for c in range(len(word)):
                    for i in range(97,123):
                        if word[c] == chr(i):
                            continue
                        newWord = word[:c] + chr(i) + word[c+1:]
                        if newWord not in wordList:
                            continue
                        if newWord in fromEnd:
                            return steps + fromEnd[newWord]
                        if newWord not in fromBegin:
                            fromBegin[newWord] = steps + 1
                            qb.append(newWord)
        return 0
