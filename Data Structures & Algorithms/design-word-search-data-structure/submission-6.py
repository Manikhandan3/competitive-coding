class TrieNode:

    def __init__(self):
        self.children = [None] * 26
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
         
        def backtrack(node, i):
            if i == len(word):
                return node.isWord
            
            if word[i] == '.':
                for child in node.children:
                    if child and backtrack(child, i+1):
                        return True
                return False
            else:
                if node.children[ord(word[i])-ord('a')]:
                    return backtrack(node.children[ord(word[i])-ord('a')], i+1)
                else:
                    return False
        
        return backtrack(self.root,0)


        
