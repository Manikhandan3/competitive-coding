class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 0
        
        if len(beginWord) != len(endWord):
            return 0
        
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        
        q = deque([beginWord])
        res = 0
        while q:
            res += 1
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for c in range(len(word)):
                    for i in range(97,123):
                        if word[c] == chr(i):
                            continue
                        newWord = word[:c] + chr(i) + word[c+1:]
                        if newWord in wordList:
                            q.append(newWord)
                            wordList.remove(newWord)
        return 0
