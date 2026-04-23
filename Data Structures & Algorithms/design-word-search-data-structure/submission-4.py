class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isWord = False
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            if not cur.children[ord(w)-ord('a')]:
                cur.children[ord(w)-ord('a')] = TrieNode()
            cur = cur.children[ord(w)-ord('a')]
        cur.isWord = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            if not root:
                return False

            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children:
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if not cur.children[ord(c)-ord('a')]:
                        return False
                    cur = cur.children[ord(c)-ord('a')]
            return cur.isWord

        return dfs(0, self.root)
        

