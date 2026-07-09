class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.is_end = True

    def search(self, word: str) -> bool:
        # Handle in this using backtracking
        # if we encounter => loop trough all children
        # recurse to each children
        # if we dont have path then we return False else we return True
        
        def dfs(root, i):
            if root.is_end and i == len(word):
                return True
            
            if i >= len(word):
                return False

            c = word[i]
            res = False
            if c == '.':
                for child in root.children:
                    res = dfs(root.children[child], i+1) or res
                return res

            if c not in root.children:
                return False
                
            return dfs(root.children[c], i+1)
        return dfs(self.root, 0)
