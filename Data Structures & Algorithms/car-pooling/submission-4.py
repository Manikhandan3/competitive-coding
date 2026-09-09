class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[1])
        i = 0
        minHeap = []
        while i < len(trips):
            cur = trips[i][1]
            while minHeap and minHeap[0][0] <= cur:
                capacity += heapq.heappop(minHeap)[1]
            while i < len(trips) and trips[i][1] == cur:
                capacity -= trips[i][0]
                if capacity < 0:
                    return False
                heapq.heappush(minHeap, [trips[i][2],trips[i][0]])
                i += 1
        return True
        