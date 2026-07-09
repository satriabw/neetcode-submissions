class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        FIRST = 97
        LAST = 123

        # We build the graph by comparing character
        graph = defaultdict(list)
        inDegree = [0] * 26

        for i in range(len(words)-1):
            first, second = words[i], words[i+1]
            j = 0

            while j < len(first) and j < len(second):
                if first[j] != second[j]:
                    graph[first[j]].append(second[j])
                    inDegree[ord(second[j]) - FIRST] += 1
                    break
                j += 1
            if len(first) > len(second) and j == len(second):
                return ""

        # Now we recheck the sort the graph
        unique_chars = set(c for word in words for c in word)
        queue = deque([c for c in unique_chars if inDegree[ord(c)-FIRST] == 0])
        visited = []

        while queue:
            char = queue.popleft()
            visited.append(char)

            for neigh in graph[char]:
                inDegree[ord(neigh)-FIRST] -= 1
                if inDegree[ord(neigh)-FIRST] == 0:
                    queue.append(neigh)
    
        return "".join(visited) if len(visited) == len(unique_chars) else ""