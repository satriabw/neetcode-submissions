class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap = []
        idx = 0
        for i, task in enumerate(tasks):
            task.append(i)
        tasks.sort()

        enqTime = tasks[0][0]
        results = []

        # Initialize heap
        while idx < len(tasks) and enqTime >= tasks[idx][0]:
            procTime = tasks[idx][1]
            realIdx = tasks[idx][2]

            heapq.heappush(heap, (procTime, realIdx))
            idx += 1
        
        # Process the task
        while idx < len(tasks) or len(heap) > 0:
            if len(heap) > 0:
                procTime, realIdx = heapq.heappop(heap)
                results.append(realIdx)
                enqTime += procTime 
            
            # New processing time
            while idx < len(tasks) and enqTime >= tasks[idx][0]:
                taskProcTime = tasks[idx][1]
                realIdx = tasks[idx][2]

                heapq.heappush(heap, (taskProcTime, realIdx))
                idx += 1

            if len(heap) == 0:
                enqTime += 1

        return results