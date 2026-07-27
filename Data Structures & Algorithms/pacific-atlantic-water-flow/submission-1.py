class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        r = len(heights)
        c = len(heights[0])

        # Pacific border
        pac = deque([])
        for i in range(r):
            if i == 0:
                for j in range(c):
                    pac.append((i, j))
            else:
                pac.append((i, 0))
        
        # Atlantic border
        atl = deque([])
        for i in range(r):
            if i == r-1:
                for j in range(c-1, -1, -1):
                    atl.append((i, j))
            else:
                atl.append((i, c-1))
        
        # Traverse the pacific
        pacVisited = set()
        while pac:
            i, j = pac.popleft()
            pacVisited.add((i, j))
            for dirI, dirJ in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nextI = i+dirI
                nextJ = j+dirJ
                if nextI >= 0 and nextJ >= 0 and nextI < r and nextJ < c and heights[nextI][nextJ] >= heights[i][j] and (nextI, nextJ) not in pacVisited:
                    pac.append((nextI, nextJ))

        atlVisited = set()
        while atl:
            i, j = atl.popleft()
            atlVisited.add((i, j))
            for dirI, dirJ in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nextI = i+dirI
                nextJ = j+dirJ
                if nextI >= 0 and nextJ >= 0 and nextI < r and nextJ < c and heights[nextI][nextJ] >= heights[i][j] and (nextI, nextJ) not in atlVisited:
                    atl.append((nextI, nextJ))
        
        result = []
        for (i, j) in atlVisited:
            if (i, j) in pacVisited:
                result.append([i, j])

        return result
         
