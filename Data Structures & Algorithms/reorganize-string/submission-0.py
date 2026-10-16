class Solution:
    def reorganizeString(self, s: str) -> str:
        count = defaultdict(int)

        for char in s:
            count[char] += 1
        
        heap = [(budget, char) for char, budget in count.items()]
        heapq.heapify_max(heap)

        prev = []
        val = []
        while heap:
            budget, char = heapq.heappop_max(heap)
            val.append(char)
            budget -= 1
            if prev and prev[0] > 0:
                heapq.heappush_max(heap, prev)
            prev = (budget, char)
            
        return ''.join(val) if len(val) == len(s) else ''
            
            
            