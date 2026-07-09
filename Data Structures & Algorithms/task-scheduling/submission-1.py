class Solution:
    import heapq
    from collections import deque
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Using heap to save task frequency first
        # Process task based on frequency, using max heap
        # After we process one task if the task is not 0, put it in buffer also track until next cycle
        # After once cycle, check if the last task is same

        buffer = deque()
        cycle = 0

        freq = {}
        for task in tasks:
            freq.setdefault(task, 0)
            freq[task] += 1

        tasks = [(freq) for _, freq in freq.items()]
        heapq.heapify_max(tasks)

        while tasks or buffer:
            while buffer and buffer[0][1] <= cycle:
                freq, _= buffer.popleft()
                heapq.heappush_max(tasks, freq)

            cycle += 1
            if tasks:
                freq = heapq.heappop_max(tasks)
                freq -= 1
                if freq > 0:
                    buffer.append((freq, cycle+n))

        return cycle