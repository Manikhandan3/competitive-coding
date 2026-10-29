class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if cur.children[ord(c)-ord('a')] is None:
                cur.children[ord(c)-ord('a')] = TrieNode()
            cur = cur.children[ord(c)-ord('a')]
        cur.isWord = True

    def search(self, word: str) -> bool:

        def dfs(i,node):
            if i == len(word):
                return node.isWord
            

            if word[i] == '.':
                for child in node.children:
                    if child:
                        if dfs(i+1,child):
                            return True
                return False
            else:
                if node.children[ord(word[i])-ord('a')]:
                    return dfs(i+1,node.children[ord(word[i])-ord('a')])
                else:
                    return False
        return dfs(0,self.root)
        
