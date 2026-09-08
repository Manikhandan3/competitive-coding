class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [task + [i] for i, task in enumerate(tasks)]
        tasks.sort()
        time = tasks[0][0]
        i = 0
        minHeap = []
        res = []
        while i < len(tasks) or minHeap:
            if i < len(tasks) and time < tasks[i][0]:
                time = tasks[i][0]
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(minHeap,[tasks[i][1],tasks[i][2]])
                i += 1
            if minHeap:
                t, index =  heapq.heappop(minHeap)
                res.append(index)
                time += t
        return res

