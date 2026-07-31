class Trie:
    def __init__(self):
        self.root = None
        self.children = {}
        self.end = False

class WordDictionary:
    def __init__(self):
        self._dict = Trie()

    def addWord(self, word: str) -> None:
        root = self._dict
        for i, w in enumerate(word):
            if w not in root.children:
                node = Trie()
                root.children[w] = node
            root = root.children[w]
        root.end = True

    def search(self, word: str) -> bool:
        root = self._dict
        return self._searchHelper(word, root)
    
    def _searchHelper(self, word, root) -> bool:
        if len(word) == 0 and root.end:
            return True
        
        if len(word) == 0:
            return False

        if word[0] in root.children:
            node = root.children[word[0]]
            return self._searchHelper(word[1:], node)
        elif word[0] == '.':
            ret = False
            for child in root.children:
                ret |= self._searchHelper(word[1:], root.children[child])
            return ret
        else:  
            return False
