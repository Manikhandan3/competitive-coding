class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            if not cur.children[ord(w)-ord('a')]:
                cur.children[ord(w)-ord('a')] = TrieNode()
            cur = cur.children[ord(w)-ord('a')]
        cur.isWord = True
        

    def search(self, word: str) -> bool:
        cur = self.root
        for w in word:
            if cur.children[ord(w)-ord('a')]:
                cur = cur.children[ord(w)-ord('a')]
            else:
                return False
        return cur.isWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for w in prefix:
            if cur.children[ord(w)-ord('a')]:
                cur = cur.children[ord(w)-ord('a')]
            else:
                return False
        return True
        
        