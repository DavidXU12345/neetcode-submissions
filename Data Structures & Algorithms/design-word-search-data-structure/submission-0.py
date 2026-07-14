class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(i, node):
            cur = node
            for j in range(i, len(word)):
                c = word[j]
                if c == '.':
                    for child in cur.children.values():
                        if dfs(j + 1, child):
                            return True
                    return False
                if c not in cur.children:
                    return False
                cur = cur.children[c]
        
            return cur.end_of_word
        return dfs(0, self.root)
        

