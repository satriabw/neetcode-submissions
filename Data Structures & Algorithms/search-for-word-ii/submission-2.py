class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False

class PrefixTree:
    def __init__(self):
        self._root = Node()      

    def insert(self, word: str) -> None:
        cur = self._root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.is_end = True

    def search(self, prefix: str) -> Tuple[bool, Any]:
        cur = self._root
        for c in prefix:
            if c not in cur.children:
                return False, None
            cur = cur.children[c]
        return True, cur

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Like a search word we try to find the first word to search first, if it exist
        # We will continue recursion as long as the word exists in prefix tree
        # While checking if it is_end or not. If the node is_end we add the word to result
        # We backtrack if the word is not in prefix tree

        # Build the prefix tree first
        prefixTree = PrefixTree()
        for word in words:
            prefixTree.insert(word)
        
        results = set()

        def backtrack(board, i, j, word, visited, node):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]) or visited[i][j] or board[i][j] not in node.children:
                return
            
            char = board[i][j]
            visited[i][j] = True
            node = node.children[char]
            word += char

            if node.is_end:
                results.add(word)

            backtrack(board, i-1, j, word, visited, node)
            backtrack(board, i+1, j, word, visited, node)
            backtrack(board, i, j-1, word, visited, node)
            backtrack(board, i, j+1, word, visited, node)
            visited[i][j] = False
        
        
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[i])):
                backtrack(board, i, j, "", visited, prefixTree._root)
        
        return list(results)


