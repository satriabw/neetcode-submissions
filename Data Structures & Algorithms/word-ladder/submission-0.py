class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # We are building a graph =>
        # Start at beginWord
        # Stop when we found endword
        # Start by changing one char in the word so O(n*26)
        # For each char we change and see whether it is exists in wordlist
        # If it add to the queue and add counter
        
        queue = deque([(beginWord, [beginWord])])
        wordList = set(wordList)

        if endWord not in wordList:
            return 0

        result = None
        while queue:
            word, path = queue.popleft()

            if word == endWord:
                result = path

            for i in range(len(word)):
                for j in range(97, 123):
                    new_word = word[:i] + chr(j) + word[i+1:]
                    if new_word in wordList:
                        queue.append((new_word, path + [new_word]))
                        wordList.remove(new_word)
            
        return len(result) if result else 0
