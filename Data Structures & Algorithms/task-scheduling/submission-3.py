class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        t = [-v for k,v in freq.items()]
        heapq.heapify(t)
        time = 0
        minHeap = []
        while t or minHeap:
            if not t:
                time = minHeap[0][0]
            
            if minHeap and minHeap[0][0] == time:
                heapq.heappush(t, heapq.heappop(minHeap)[1])
            
            node = heapq.heappop(t)
            time += 1
            if node < -1:
                heapq.heappush(minHeap, [time+n,node+1])
        return time

