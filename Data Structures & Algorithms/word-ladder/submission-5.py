class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 0
        
        if len(beginWord) != len(endWord):
            return 0
        
        wordList = set(wordList)
        visited = set()
        if endWord not in wordList:
            return 0
        
        # qb, qe = deque([beginWord]), deque([endWord])
        fromBegin, fromEnd = {beginWord}, {endWord}
        steps = 0
        while fromBegin and fromEnd:
            if len(fromBegin) > len(fromEnd):
                # qb, qe = qe, qb
                fromBegin, fromEnd = fromEnd, fromBegin
            temp = set()
            steps += 1
            for word in fromBegin:
                visited.add(word)
                for c in range(len(word)):
                    for i in range(97,123):
                        if word[c] == chr(i):
                            continue
                        newWord = word[:c] + chr(i) + word[c+1:]
                        # if newWord not in wordList:
                        #     continue
                        if newWord in fromEnd:
                            return steps + 1
                        if newWord not in wordList or newWord in visited:
                            continue
                        # if newWord not in fromBegin:
                        temp.add(newWord)
                        # qb.append(newWord)
                fromBegin = temp
        return 0
